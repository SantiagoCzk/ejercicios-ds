import { useState } from 'react';
import CrearEstudiante from '../crearEstudiante/crear_estudiante';
import styles from './menu_funcionalidad.module.css';

export default function MenuFuncionalidad() {
  const [showForm, setShowForm] = useState(false);

  return (
    <div className={styles.container}>
      <button
        className={styles.btnToggle}
        onClick={() => setShowForm((s) => !s)}
      >
        {showForm ? 'Ocultar formulario' : 'Crear Estudiante'}
      </button>

      {showForm && (
        <div className={styles.container}>
          <CrearEstudiante />
        </div>
      )}
    </div>
  );
}