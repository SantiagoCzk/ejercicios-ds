
import * as React from 'react'
import { useState } from 'react';
import styles from './crear_estudiante.module.css';

export default function CrearEstudiante() {
  const [nombre, setNombre] = useState('');
  const [legajo, setLegajo] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const nombreValido = /^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{1,50}$/.test(nombre);
    const legajoNum = Number(legajo);
    const legajoValido = Number.isInteger(legajoNum) && legajoNum > 0;

    if (!nombreValido || !legajoValido) {
      setError('Nombre o legajo inválidos');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const res = await fetch(
        'http://127.0.0.1:8000/estudiantes/',
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ nombre, legajo: legajoNum }),
        },
      );

      if (!res.ok) {
        const msg = await res.text();
        throw new Error(msg || 'Error al crear estudiante');
      }

      setSuccess(true);
      setNombre('');
      setLegajo('');
    } catch (err: any) {
      setError(err.message || 'Error inesperado');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className={styles.formContainer}>
      <div className={styles.formControl}>
        <label htmlFor="nombre" className={styles.label}>Nombre</label>
        <input
          id="nombre"
          type="text"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          required
          className={styles.input}
        />
      </div>

      <div className={styles.formControl}>
        <label htmlFor="legajo" className={styles.label}>Legajo</label>
        <input
          id="legajo"
          type="number"
          min="1"
          step="1"
          value={legajo}
          onChange={(e) => setLegajo(e.target.value)}
          required
          className={styles.input}
        />
      </div>

      <button type="submit" disabled={loading} className={styles.btn}>
        {loading ? 'Creando…' : 'Crear Estudiante'}
      </button>

      {success && <p className={styles.msgSuccess}>Estudiante creado correctamente</p>}
      {error && <p className={styles.msgError}>{error}</p>}
    </form>
  );
}