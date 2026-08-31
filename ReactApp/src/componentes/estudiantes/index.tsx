import MenuFuncionalidad from './menuFuncionalidad/menu_funcionalidad';
import './index.module.css'

export default function Estudiantes() {
  return (
    <section id="estudiantes">
      <h1 className=''>Estudiantes</h1>

      {/* Botón + formulario de creación */}
      <MenuFuncionalidad />

      {/* Resto del contenido de la vista permanece sin tocar */}
    </section>
  );
}