const notifica = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/estudio/consulta/"); 
        const data = response.json();
        var num = 0;
        var array = [];
        var texto = "";

        data.then(function(value){
            arreglo = value.preguntas;
            notifi.innerText = arreglo.length;

            // Cuando modifico el js en visual studio, no se modifica en el navegador

            arreglo.forEach(el => {
               console.log("HOla"); 
            });
        });

    } catch (error){
        console.log(error);
    }
};

const carga = async () => {
    await notifica();
}

window.addEventListener("load", async () => {
    await carga();
})
