import { useState } from 'react';
import './App.css';

/* Importamos los componentes de sección */
import Estudiantes from './componentes/estudiantes';
import Profesores from './componentes/profesores';
import Cursos from './componentes/cursos';

function App() {
  /* Estado que controla la sección activa */
  const [active, setActive] = useState<'estudiantes' | 'profesores' | 'cursos'>(
    'estudiantes'
  );

  return (
    <>
      {/* Menú de navegación */}
      <nav className="menu">
        <ul className="nav-list">
          <li>
            <button onClick={() => setActive('estudiantes')} className={active === 'estudiantes' ? 'active' : ''}>
              Estudiantes
            </button>
          </li>
          <li>
            <button onClick={() => setActive('profesores')} className={active === 'profesores' ? 'active' : ''}>
              Profesores
            </button>
          </li>
          <li>
            <button onClick={() => setActive('cursos')} className={active === 'cursos' ? 'active' : ''}>
              Cursos
            </button>
          </li>
        </ul>
      </nav>

      {/* Renderizado de la sección activa */}
      <div className="content">
        {active === 'estudiantes' && <Estudiantes />}
        {active === 'profesores' && <Profesores />}
        {active === 'cursos' && <Cursos />}
      </div>
    </>
  );
}

export default App;


/*
import { useState } from 'react'
import './App.css'
import Estudiante from './componentes/estudiantes'
import Profesores from './componentes/profesores'
import Cursos from './componentes/cursos'
 
function App() {

  const [active, setActive] = useState<'estudiantes' | 'profesores' | 'cursos'>('estudiantes')

  return (
    <>
        <nav className="menu">
          <ul className="nav-list">
            <li><button onClick={() => setActive('estudiantes')} className={active==='estudiantes'?'active':''}>Estudiantes</button></li>
            <li><button onClick={() => setActive('profesores')} className={active==='profesores'?'active':''}>Profesores</button></li>
            <li><button onClick={() => setActive('cursos')} className={active==='cursos'?'active':''}>Cursos</button></li>
          </ul>
        </nav>


    <section id="content">
  {active === 'estudiantes' && <Estudiante />}
  {active === 'profesores' && <Profesores />}
  {active === 'cursos' && <Cursos />}
</section>
</>
  )
}

export default App
*/