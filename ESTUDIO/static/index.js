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

            arreglo.forEach(el => {
                texto += `Ya puedes repasar la pregunta ${el.name}\n`;
            });

            seccion.innerText = texto;

        });

    } catch (error){
        console.log(error);
    }
};

window.addEventListener("load", async () => {
    await notifica();
})
