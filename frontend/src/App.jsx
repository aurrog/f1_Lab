import { useEffect, useState } from 'react'
import './App.css'

const API_BASE_URL = 'http://127.0.0.1:8000'

function App() {
  const [races, setRaces] = useState([])
  const [drivers, setDrivers] = useState([])

  const [selectedRace, setSelectedRace] = useState('')
  const [selectedDriver, setSelectedDriver] = useState('')
  const [selectedStrategy, setSelectedStrategy] = useState('')

  const [loadingRaces, setLoadingRaces] = useState(true)
  const [loadingDrivers, setLoadingDrivers] = useState(false)

  const [racesError, setRacesError] = useState('')
  const [driversError, setDriversError] = useState('')

  const [simulationStarted, setSimulationStarted] = useState(false)

  useEffect(() => {
    async function loadRaces() {
      try {
        setLoadingRaces(true)
        setRacesError('')

        const response = await fetch(`${API_BASE_URL}/api/v1/races/`)

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`)
        }

        const data = await response.json()

        setRaces(data)
      } catch (error) {
        console.error('Failed to load races:', error)
        setRacesError('Could not load races from the backend.')
      } finally {
        setLoadingRaces(false)
      }
    }

    loadRaces()
  }, [])

  useEffect(() => {
    if (!selectedRace) {
      setDrivers([])
      setSelectedDriver('')
      return
    }

    async function loadDrivers() {
      try {
        setLoadingDrivers(true)
        setDriversError('')
        setSelectedDriver('')

        const response = await fetch(
          `${API_BASE_URL}/api/v1/drivers/?session_key=${selectedRace}`
        )

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`)
        }

        const data = await response.json()

        setDrivers(data)
      } catch (error) {
        console.error('Failed to load drivers:', error)
        setDriversError('Could not load drivers for this race.')
        setDrivers([])
      } finally {
        setLoadingDrivers(false)
      }
    }

    loadDrivers()
  }, [selectedRace])

  function handleRaceChange(event) {
    setSelectedRace(event.target.value)
    setSimulationStarted(false)
  }

  function handleDriverChange(event) {
    setSelectedDriver(event.target.value)
    setSimulationStarted(false)
  }

  function handleStrategyChange(event) {
    setSelectedStrategy(event.target.value)
    setSimulationStarted(false)
  }

  function handleSimulation() {
    if (!selectedRace || !selectedDriver || !selectedStrategy) {
      return
    }

    setSimulationStarted(true)
  }

  const selectedRaceData = races.find(
    (race) => String(race.session_key) === selectedRace
  )

  const selectedDriverData = drivers.find(
    (driver) => String(driver.driver_number) === selectedDriver
  )

  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">
          F1 <span>STRATEGY LAB</span>
        </div>

        <nav>
          <a href="#simulator">Simulator</a>
          <a href="#results">Results</a>
          <a href="#about">About</a>
        </nav>
      </header>

      <main>
        <section className="hero">
          <div className="hero-content">
            <p className="eyebrow">FORMULA 1 • STRATEGY ANALYSIS</p>

            <h1>
              Think like a
              <span> race strategist.</span>
            </h1>

            <p className="hero-text">
              Simulate race strategies, compare different scenarios
              and explore how decisions can change the outcome of a race.
            </p>

            <a href="#simulator" className="hero-button">
              Start simulation
            </a>
          </div>

          <div className="hero-card">
            <div className="card-top">
              <span>RACE SIMULATION</span>
              <span className="status">● READY</span>
            </div>

            <div className="race-name">
              {selectedRaceData
                ? selectedRaceData.session_name
                : 'Choose a race'}
            </div>

            <div className="race-info">
              <div>
                <strong>—</strong>
                <small>LAPS</small>
              </div>

              <div>
                <strong>—</strong>
                <small>STINTS</small>
              </div>

              <div>
                <strong>∞</strong>
                <small>SCENARIOS</small>
              </div>
            </div>

            <div className="strategy-line">
              <span>SOFT</span>
              <span>→</span>
              <span>MEDIUM</span>
              <span>→</span>
              <span>MEDIUM</span>
            </div>
          </div>
        </section>

        <section id="simulator" className="section">
          <div className="section-heading">
            <p className="eyebrow">01 / SIMULATION</p>
            <h2>Strategy Simulator</h2>
            <p>
              Configure a race and run a strategy simulation.
            </p>
          </div>

          <div className="simulator-grid">
            <div className="panel">
              <label htmlFor="race">Race</label>

              <select
                id="race"
                value={selectedRace}
                onChange={handleRaceChange}
                disabled={loadingRaces}
              >
                <option value="">
                  {loadingRaces ? 'Loading races...' : 'Choose a race'}
                </option>

                {races.map((race) => (
                  <option
                    key={race.session_key}
                    value={race.session_key}
                  >
                    {race.session_name} — {race.location}
                  </option>
                ))}
              </select>

              {racesError && (
                <p className="api-error">
                  {racesError}
                </p>
              )}
            </div>

            <div className="panel">
              <label htmlFor="driver">Driver</label>

              <select
                id="driver"
                value={selectedDriver}
                onChange={handleDriverChange}
                disabled={!selectedRace || loadingDrivers}
              >
                <option value="">
                  {!selectedRace
                    ? 'Choose a race first'
                    : loadingDrivers
                      ? 'Loading drivers...'
                      : 'Choose a driver'}
                </option>

                {drivers.map((driver) => (
                  <option
                    key={driver.driver_number}
                    value={driver.driver_number}
                  >
                    #{driver.driver_number} {driver.full_name} —{' '}
                    {driver.team_name}
                  </option>
                ))}
              </select>

              {driversError && (
                <p className="api-error">
                  {driversError}
                </p>
              )}
            </div>

            <div className="panel">
              <label htmlFor="strategy">Strategy</label>

              <select
                id="strategy"
                value={selectedStrategy}
                onChange={handleStrategyChange}
              >
                <option value="">Choose a strategy</option>
                <option value="one-stop">One Stop</option>
                <option value="two-stop">Two Stop</option>
                <option value="three-stop">Three Stop</option>
              </select>
            </div>

            <button
              className="simulate-button"
              onClick={handleSimulation}
              disabled={
                !selectedRace ||
                !selectedDriver ||
                !selectedStrategy
              }
            >
              Run simulation →
            </button>
          </div>

          {selectedDriverData && (
            <div className="selected-driver-preview">
              <div
                className="driver-color"
                style={{
                  backgroundColor: `#${selectedDriverData.team_colour}`,
                }}
              />

              <div>
                <span className="selected-driver-label">
                  SELECTED DRIVER
                </span>

                <strong>
                  #{selectedDriverData.driver_number}{' '}
                  {selectedDriverData.full_name}
                </strong>

                <span>
                  {selectedDriverData.team_name}
                </span>
              </div>
            </div>
          )}
        </section>

        <section id="results" className="section results-section">
          <div className="section-heading">
            <p className="eyebrow">02 / RESULTS</p>
            <h2>Simulation Results</h2>

            <p>
              {simulationStarted
                ? 'Simulation configuration is ready.'
                : 'Your results will appear here after running a simulation.'}
            </p>
          </div>

          {simulationStarted ? (
            <div className="simulation-summary">
              <div>
                <span>RACE</span>
                <strong>
                  {selectedRaceData?.session_name}
                </strong>
              </div>

              <div>
                <span>DRIVER</span>
                <strong>
                  #{selectedDriverData?.driver_number}{' '}
                  {selectedDriverData?.full_name}
                </strong>
              </div>

              <div>
                <span>STRATEGY</span>
                <strong>
                  {selectedStrategy === 'one-stop'
                    ? 'One Stop'
                    : selectedStrategy === 'two-stop'
                      ? 'Two Stop'
                      : 'Three Stop'}
                </strong>
              </div>

              <p className="simulation-note">
                Backend simulation results will be connected here next.
              </p>
            </div>
          ) : (
            <div className="empty-results">
              <div className="empty-icon">◎</div>

              <h3>No simulation yet</h3>

              <p>
                Configure your race strategy above and start the simulation.
              </p>
            </div>
          )}
        </section>

        <section id="about" className="about">
          <p className="eyebrow">F1 STRATEGY LAB</p>

          <h2>Data. Strategy. Decisions.</h2>

          <p>
            A project for exploring Formula 1 race strategy through
            simulation, data analysis and scenario comparison.
          </p>
        </section>
      </main>

      <footer>
        <span>F1 STRATEGY LAB</span>
        <span>Built for strategy analysis</span>
      </footer>
    </div>
  )
}

export default App