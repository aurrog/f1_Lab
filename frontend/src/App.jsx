import { useState } from 'react'
import './App.css'

function App() {
  const [selectedDriver, setSelectedDriver] = useState(null)

  const drivers = [
    {
      name: 'Lando Norris',
      team: 'McLaren',
      number: '4',
      color: '#ff8000',
    },
    {
      name: 'Oscar Piastri',
      team: 'McLaren',
      number: '81',
      color: '#ff8000',
    },
    {
      name: 'Lewis Hamilton',
      team: 'Ferrari',
      number: '44',
      color: '#e8002d',
    },
    {
      name: 'Max Verstappen',
      team: 'Red Bull Racing',
      number: '1',
      color: '#3671c6',
    },
  ]

  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">F1 STRATEGY LAB</div>

        <nav>
          <a href="#simulator">Simulator</a>
          <a href="#results">Results</a>
          <a href="#about">About</a>
        </nav>
      </header>

      <main>
        {/* HERO */}

        <section className="hero">
          <div className="hero-background">
            <div className="track-line track-line-1"></div>
            <div className="track-line track-line-2"></div>
            <div className="track-line track-line-3"></div>
            <div className="hero-circle"></div>
            <div className="hero-cross hero-cross-1">+</div>
            <div className="hero-cross hero-cross-2">+</div>
          </div>

          <div className="hero-content">
            <span className="eyebrow">
              FORMULA 1 · STRATEGY SIMULATION
            </span>

            <h1>
              THINK LIKE A
              <br />
              <span>RACE STRATEGIST.</span>
            </h1>

            <p>
              Explore race strategies, compare tyre choices and simulate
              different scenarios before the lights go out.
            </p>

            <a href="#simulator" className="hero-button">
              START SIMULATION
              <span>→</span>
            </a>
          </div>

          <div className="hero-data">
            <div className="data-top">
              <span>F1SL / 01</span>
              <span>LIVE SIMULATION</span>
            </div>

            <div className="data-number">53</div>

            <div className="data-bottom">
              <div>
                <span>RACE</span>
                <strong>MONZA</strong>
              </div>

              <div>
                <span>LAPS</span>
                <strong>53</strong>
              </div>

              <div>
                <span>SCENARIOS</span>
                <strong>∞</strong>
              </div>
            </div>
          </div>

          <div className="scroll-indicator">
            <span>SCROLL TO EXPLORE</span>
            <div></div>
          </div>
        </section>

        {/* SIMULATOR */}

        <section className="simulator" id="simulator">
          <div className="section-heading">
            <span>01</span>

            <div>
              <p>SIMULATION SETUP</p>
              <h2>Choose your driver</h2>
            </div>
          </div>

          <div className="driver-grid">
            {drivers.map((driver) => (
              <button
                key={driver.number}
                className={`driver-card ${
                  selectedDriver?.number === driver.number ? 'selected' : ''
                }`}
                style={{
                  '--team-color': driver.color,
                }}
                onClick={() => setSelectedDriver(driver)}
              >
                <span className="driver-number">{driver.number}</span>

                <div className="driver-info">
                  <p className="driver-team">{driver.team}</p>
                  <h3>{driver.name}</h3>
                </div>

                <span className="driver-arrow">↗</span>
              </button>
            ))}
          </div>

          {selectedDriver && (
            <div
              className="selected-driver"
              style={{
                '--team-color': selectedDriver.color,
              }}
            >
              <div>
                <span>SELECTED DRIVER</span>
                <h3>{selectedDriver.name}</h3>
              </div>

              <p>
                {selectedDriver.team} · #{selectedDriver.number}
              </p>
            </div>
          )}

          <div className="setup-grid">
            <div className="setup-block">
              <label>RACE</label>

              <select defaultValue="Italian Grand Prix">
                <option>Italian Grand Prix</option>
                <option>British Grand Prix</option>
                <option>Belgian Grand Prix</option>
                <option>Japanese Grand Prix</option>
              </select>
            </div>

            <div className="setup-block">
              <label>STARTING TYRE</label>

              <select defaultValue="Soft">
                <option>Soft</option>
                <option>Medium</option>
                <option>Hard</option>
              </select>
            </div>

            <div className="setup-block">
              <label>STRATEGY</label>

              <select defaultValue="S → M → M">
                <option>S → M → M</option>
                <option>M → H → M</option>
                <option>S → M → H</option>
                <option>M → M → H</option>
              </select>
            </div>
          </div>

          <button className="simulate-button">
            RUN SIMULATION <span>→</span>
          </button>
        </section>

        {/* RESULTS */}

        <section className="results" id="results">
          <div className="section-heading">
            <span>02</span>

            <div>
              <p>SIMULATION OUTPUT</p>
              <h2>Race results</h2>
            </div>
          </div>

          <div className="results-empty">
            <span>—</span>
            <h3>No simulation yet</h3>

            <p>
              Choose a driver and strategy above to see the simulated
              race outcome.
            </p>
          </div>
        </section>

        {/* ABOUT */}

        <section className="about" id="about">
          <div className="section-heading">
            <span>03</span>

            <div>
              <p>ABOUT THE PROJECT</p>
              <h2>F1 Strategy Lab</h2>
            </div>
          </div>

          <p className="about-text">
            F1 Strategy Lab is an experimental racing strategy simulator.
            It combines Formula 1 race data, strategy modelling and
            probabilistic simulation to explore how different decisions
            can affect a race.
          </p>
        </section>
      </main>

      <footer>
        <span>F1 STRATEGY LAB</span>
        <span>Built with React</span>
      </footer>
    </div>
  )
}

export default App