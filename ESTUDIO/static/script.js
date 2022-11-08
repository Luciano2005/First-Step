// variables

let workTittle = document.getElementById('work');
let breakTittle = document.getElementById('break');

let workTime = 25;
let breakTime = 5;

let seconds = "00"

// mostrar
window.onload = () => {
    document.getElementById('minutes').innerHTML = workTime;
    document.getElementById('seconds').innerHTML = seconds;

    workTittle.classList.add('active');
}

// iniciar temporizador
function start() {
    // cambiar boton            
    document.getElementById('start').style.display = "none";
    document.getElementById('reset').style.display = "block";

    // cambiar tiempo
    seconds = 59;

    let workMinutes = workTime - 1;
    let breakMinutes = breakTime - 1;

    breakCount = 0;

    // cuenta regresiva
    let timerFunction = () => {
        //cambiar lo mostrado
        document.getElementById('minutes').innerHTML = workMinutes;
        document.getElementById('seconds').innerHTML = seconds;

        // iniciar
        seconds = seconds - 1;

        if(seconds === 0) {
            workMinutes = workMinutes - 1;
            if(workMinutes === -1 ){
                if(breakCount % 2 === 0) {
                    // inicio receso
                    workMinutes = breakMinutes;
                    breakCount++

                    // cambiar painel
                    workTittle.classList.remove('active');
                    breakTittle.classList.add('active');
                }else {
                    // seguir trabajo
                    workMinutes = workTime;
                    breakCount++

                    // cambiar painel
                    breakTittle.classList.remove('active');
                    workTittle.classList.add('active');
                }
            }
            seconds = 59;
        }
    }

    // inicio de temporizador
    setInterval(timerFunction, 1000); // 1000 = 1sec
}