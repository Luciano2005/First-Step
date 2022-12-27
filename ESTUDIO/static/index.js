const notifica = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/estudio/consulta/"); 
        const data = response.json();
        var num = 0;
        var array = [];

        data.then(function(value){
            arreglo = value.preguntas;
        
            arreglo.forEach(element => {
                num += 1;
            });

            notifi.innerText = num;

        });

    } catch (error){
        console.log(error);
    }
};

window.addEventListener("load", async () => {
    await notifica();
})
