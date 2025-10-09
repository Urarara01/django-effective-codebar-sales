// --- fetch, then, catch, async/await, try/catch ---
const apiForm = document.getElementById('apiForm');
const apiResult = document.getElementById('apiResult');

apiForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const nombre = document.getElementById('nombre').value;
    const edad = document.getElementById('edad').value;
    try {
        const response = await fetch('/js_practice/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ nombre, edad })
        });
        const data = await response.json();
        apiResult.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        apiResult.textContent = 'Error: ' + error;
    }
});

// --- Utilidad para CSRF (Django) ---
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// --- Zona de pruebas JS ---
const jsInput = document.getElementById('jsInput');
const jsOutput = document.getElementById('jsOutput');
document.getElementById('runJs').addEventListener('click', function() {
    try {
        // eslint-disable-next-line no-eval
        const result = eval(jsInput.value);
        jsOutput.textContent = typeof result === 'undefined' ? 'Sin resultado (undefined)' : result;
    } catch (err) {
        jsOutput.textContent = 'Error: ' + err;
    }
});

// Ejemplo de uso de forEach, map, JSON.stringify, JSON.parse, createElement, appendChild, innerHTML, remove
// Puedes probar en la zona de pruebas JS:
// let arr = [1,2,3]; arr.forEach(x => console.log(x));
// let dobles = arr.map(x => x*2); JSON.stringify(dobles);
// let obj = {a:1}; let texto = JSON.stringify(obj); JSON.parse(texto);
// let div = document.createElement('div'); div.innerHTML = 'Hola'; document.body.appendChild(div); div.remove();
//
// Ejemplos útiles para practicar en la zona de pruebas JS:
//
// --- forEach ---
// let arr = [1, 2, 3];
// arr.forEach(x => console.log('Elemento:', x));
//
// --- map ---
// let dobles = arr.map(x => x * 2); dobles;
//
// --- JSON.stringify y JSON.parse ---
// let obj = {nombre: 'Ana', edad: 25};
// let texto = JSON.stringify(obj); texto;
// let obj2 = JSON.parse(texto); obj2;
//
// --- createElement, appendChild, innerHTML, remove ---
// let div = document.createElement('div');
// div.innerHTML = '<b>Hola desde JS</b>';
// document.body.appendChild(div);
// setTimeout(() => div.remove(), 2000);
//
// --- fetch con async/await ---
// async function enviar() {
//   let resp = await fetch('/js_practice/api/', {
//     method: 'POST',
//     headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
//     body: JSON.stringify({nombre: 'Test', edad: 99})
//   });
//   let data = await resp.json();
//   return data;
// }
// enviar().then(console.log);
//
// --- try/catch ---
// try {
//   throw new Error('¡Esto es un error!');
// } catch(e) {
//   console.log('Capturado:', e.message);
// }
//
// Puedes copiar y pegar estos ejemplos en la zona de pruebas JS para ver cómo funcionan.
