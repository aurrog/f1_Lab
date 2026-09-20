import './App.css'

function App() {
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
              Italian Grand Prix
            </div>

            <div className="race-info">
              <div>
                <strong>53</strong>
                <small>LAPS</small>
              </div>

              <div>
                <strong>3</strong>
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

              <select id="race">
                <option>Choose a race</option>
                <option>Monaco Grand Prix</option>
                <option>British Grand Prix</option>
                <option>Italian Grand Prix</option>
              </select>
            </div>

            <div className="panel">
              <label htmlFor="driver">Driver</label>

              <select id="driver">
                <option>Choose a driver</option>
                <option>Lewis Hamilton</option>
                <option>Lando Norris</option>
                <option>Max Verstappen</option>
                <option>George Russell</option>
              </select>
            </div>

            <div className="panel">
              <label htmlFor="strategy">Strategy</label>

              <select id="strategy">
                <option>Choose a strategy</option>
                <option>One Stop</option>
                <option>Two Stop</option>
                <option>Three Stop</option>
              </select>
            </div>

            <button className="simulate-button">
              Run simulation →
            </button>
          </div>
        </section>

        <section id="results" className="section results-section">
          <div className="section-heading">
            <p className="eyebrow">02 / RESULTS</p>
            <h2>Simulation Results</h2>
            <p>
              Your results will appear here after running a simulation.
            </p>
          </div>

          <div className="empty-results">
            <div className="empty-icon">◎</div>
            <h3>No simulation yet</h3>
            <p>
              Configure your race strategy above and start the simulation.
            </p>
          </div>
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