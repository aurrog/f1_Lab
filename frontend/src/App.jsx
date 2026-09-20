import './App.css'

function App() {
  return (
    <div>
      <header>
        <h1>F1 Strategy Lab</h1>
        <p>Formula 1 Race Strategy Simulator</p>
      </header>

      <main>
        <section>
          <h2>Strategy Simulator</h2>

          <p>
            Simulate race strategies and analyze possible outcomes.
          </p>

          <label>
            Race
            <select>
              <option>Choose a race</option>
              <option>Monaco Grand Prix</option>
              <option>British Grand Prix</option>
              <option>Italian Grand Prix</option>
            </select>
          </label>

          <button>
            Start simulation
          </button>
        </section>

        <section>
          <h2>Simulation results</h2>

          <p>
            Your simulation results will appear here.
          </p>
        </section>
      </main>
    </div>
  )
}

export default App