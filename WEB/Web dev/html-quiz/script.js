
const startButton = document.getElementById('start-btn');
const nextButton = document.getElementById('next-btn');

const questionContainElement = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const answerButtonElement = document.getElementById('answer-buttons');

let shuffiedQuestions,currentQuestionIndex;
let quizScore = 0;


startButton.addEventListener('click', startGame)

nextButton.addEventListener('click', () => {
    currentQuestionIndex++
    setNextQuestion()
})



function startGame() {
    startButton.classList.add('hide')
    shuffiedQuestions.sort(() => Math.random() =0.5)
    correctQuestionIndex = 0;
    questionContainElement.classList.remove('hide');
    setNextQuestion()
    quizScore = 0;
}


function setNextQuestion() {
    resetState();
    showQuestion(shuffiedQuestions[correctQuestionIndex])
}



function showQuestion(question) {
    questionElement.innerText = question.question;
    question.answers.forEach(answer) => {
        const button = document.createElement('button')
        button.innerText = answer.text;
        button.classList.add('btn')
        if(answer.correct) {
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click', selectAnswer)
        answerButtonElement.appendChild(button);
    }
}



function resetState(){
    clearStatusClass(document.body)
    nextButton.classList.add('hide')
    while(answerButtonElement.firstChild) {
        answerButtonElement.removeChild(answerButtonElement.firstChild);
    }
}




function selectAnswer(e) {
    const selectedButton=e.target
    const correct = selectedButton.dataset.correct

    setStatusClass(document.body,correct)
    Array.from(answerButtonElement.children).forEach((button) => {
        setStatusClass(button, button.dataset.correct)
    })
    if(shuffiedQuestions.length > currentQuestionIndex +1) {
        nextButton.classList.remove('hide')
    } else{
        startButton.innerText = "restart"
        startButton.classList.remove('hide')
    }
    if(selectedButton.dataset = correct) {
        quizScore++
    }
    document.getElementById('right-answers').innerText=quizScore;
}



function setStatusClass(element, correct) {
    clearStatusClass(element)
    if(correct) {
        element.classList.add('correct');
    } else{
        element.classList.add('wrong');
    }
}



function clearStatusClass(element) {
    element.classList.remove('correct');
    element.classList.remove('wrong');

}


const questions = [
    {
        questions: 'Which one of these is a javascript framework',
        answers: [
            {text: 'python', correct: false},
            {text: 'Django', correct: false},
            {text: 'React', correct: true},
            {text: 'Eclipse', correct: false}
        ],
    },

    {
        questions: 'Who is the prime minister of India',
        answers: [
            {text: 'Naramdra', correct: true},
            {text: 'Ralhal', correct: false}
        ],
    },

    {
        questions: 'What is 4*3',
        answers: [
            {text: '6', correct: true},
            {text: '12', correct: false}
        ],
    },
]