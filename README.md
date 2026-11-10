# Links cortos de CIMA

Todo lo que se comparte con una marca, una creadora o el equipo sale de acá.
**Nunca se pasa el link largo de `cleargy.ugc` o `cleargy.dashboard`.**

| Para qué | Link |
|---|---|
| Collab · registro | `cima-creators.github.io/<marca>` |
| Collab · app de la creadora | `cima-creators.github.io/<marca>/app` |
| Collab · panel | `cima-creators.github.io/<marca>/panel` |
| UGC · app de creadoras (suben los videos) | `cima-creators.github.io/<marca>/videos` |
| UGC · panel de la marca | `cima-creators.github.io/<marca>/admin` |
| Vista General (interna, solo CIMA) | `cima-creators.github.io/vista` |

Cada carpeta es un redirect de tres líneas a la página de siempre; conserva los
parámetros que vengan (`t=`, `ref=`, `ver=`, `creador=`) y agrega un `v=` para
que el celular no sirva la copia vieja.

- **Collabs** (`/<marca>`, `/app`, `/panel`, `/demo`): los arma el chat "App UGC (Canjes)"
  copiando una carpeta y cambiando el slug.
- **UGC** (`/<marca>/videos`, `/<marca>/admin`): `python3 build-links.py [ruta/a/cima-admin.html]`
  los regenera para todas las marcas que estén en el panel. Marca nueva → correrlo y pushear.
- **Guiones** (`/<marca>/guiones`): acá no es un redirect, es la página misma. La marca y sus creadoras ven los guiones
  aprobados al lado del anuncio de referencia; cada una entra con su clave y la creadora ve solo los suyos. La página no
  trae claves ni guiones: cada clave abre su paquete cifrado (`d/<id>.json`, AES-256-GCM); `v/` son los anuncios de
  referencia. **No se edita a mano**: se arma con `creativos/formatos/cliente.py <marca> --aprobados <revisión> --github
  <este repo>/<marca>/guiones` desde la carpeta de trabajo de CIMA. Un guion puntual se abre con `#g-<código>`.
