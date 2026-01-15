const PraxisQuiz = {
  state: {
    timeRemaining: null,
    timerId: null,
    quizId: null,
    questions: [],
    currentIndex: 0,
  },
  startTimer(seconds, resultsUrl) {
    if (this.state.timerId) {
      clearInterval(this.state.timerId);
    }
    this.state.timeRemaining = seconds;
    this.state.resultsUrl = resultsUrl;

    // If timer already expired, redirect immediately
    if (this.state.timeRemaining <= 0) {
      if (resultsUrl) {
        window.location.href = resultsUrl;
      }
      return;
    }

    this.state.timerId = setInterval(() => {
      this.state.timeRemaining -= 1;
      const timerDisplay = document.querySelector("[data-timer-display]");
      if (timerDisplay) {
        timerDisplay.textContent = `${this.state.timeRemaining}s`;
      }
      if (this.state.timeRemaining <= 0) {
        clearInterval(this.state.timerId);
        // Redirect to results when timer expires
        if (this.state.resultsUrl) {
          window.location.href = this.state.resultsUrl;
        }
      }
    }, 1000);
  },
  loadQuestions(questions, quizId) {
    this.state.questions = questions;
    this.state.quizId = quizId;
    this.state.currentIndex = 0;
  },
  currentQuestion() {
    return this.state.questions[this.state.currentIndex];
  },
  hasNextQuestion() {
    return this.state.currentIndex < this.state.questions.length - 1;
  },
  nextQuestion() {
    if (this.hasNextQuestion()) {
      this.state.currentIndex += 1;
      return true;
    }
    return false;
  },
};

document.addEventListener("DOMContentLoaded", () => {
  const timerDisplay = document.querySelector("[data-timer-display]");
  const quizDataElement = document.querySelector("[data-quiz-data]");
  const quizContainer = document.querySelector("[data-quiz-container]");
  const questionText = document.querySelector("[data-question-text]");
  const codeContainer = document.querySelector("[data-code-container]");
  const codeBlock = document.querySelector("[data-code-block]");
  const optionsContainer = document.querySelector("[data-question-options]");
  const feedbackContainer = document.querySelector("[data-quiz-feedback]");
  const nextButton = document.querySelector("[data-next-question]");
  const progressLabel = document.querySelector("[data-quiz-progress]");
  const timerSeconds = quizContainer ? Number(quizContainer.dataset.quizTimer) : null;
  const submitUrl = quizContainer ? quizContainer.dataset.submitUrl : null;
  const resultsUrl = quizContainer ? quizContainer.dataset.resultsUrl : null;

  if (!quizDataElement || !quizContainer || !submitUrl || !resultsUrl) {
    return;
  }

  if (timerDisplay && timerSeconds) {
    PraxisQuiz.startTimer(timerSeconds, resultsUrl);
  }

  const quizData = JSON.parse(quizDataElement.textContent || "[]");
  const quizId = Number(quizContainer.dataset.quizId);
  PraxisQuiz.loadQuestions(quizData, quizId);

  const renderQuestion = () => {
    const question = PraxisQuiz.currentQuestion();
    if (!question) {
      return;
    }
    questionText.textContent = question.question_text;
    if (question.code_snippet) {
      codeContainer.hidden = false;
      codeBlock.textContent = question.code_snippet;
      if (window.PraxisSyntaxHighlighter) {
        window.PraxisSyntaxHighlighter.applyHighlighting(codeBlock);
      }
    } else {
      codeContainer.hidden = true;
      codeBlock.textContent = "";
    }

    optionsContainer.innerHTML = "";
    Object.entries(question.options).forEach(([key, value]) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "praxis-button praxis-option-button";
      button.dataset.option = key;
      button.textContent = `${key}. ${value}`;
      optionsContainer.appendChild(button);
    });

    feedbackContainer.textContent = "";
    nextButton.disabled = true;
    nextButton.textContent = PraxisQuiz.hasNextQuestion() ? "Next question" : "View results";
    progressLabel.textContent = `Question ${PraxisQuiz.state.currentIndex + 1} of ${PraxisQuiz.state.questions.length}`;
  };

  const submitAnswer = async (questionId, answer) => {
    const response = await fetch(submitUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        quiz_id: PraxisQuiz.state.quizId,
        question_id: questionId,
        user_answer: answer,
      }),
    });
    if (!response.ok) {
      throw new Error("Failed to submit answer");
    }
    return response.json();
  };

  optionsContainer.addEventListener("click", async (event) => {
    const button = event.target.closest("button[data-option]");
    if (!button) {
      return;
    }
    const question = PraxisQuiz.currentQuestion();
    if (!question) {
      return;
    }
    optionsContainer.querySelectorAll("button").forEach((option) => {
      option.disabled = true;
    });
    try {
      const result = await submitAnswer(question.id, button.dataset.option);
      const status = result.is_correct ? "Correct" : "Incorrect";
      feedbackContainer.textContent = result.is_correct
        ? `${status}.`
        : `${status}. Correct answer: ${result.correct_answer}.`;
      nextButton.disabled = false;
    } catch (error) {
      feedbackContainer.textContent = "Unable to submit answer. Please try again.";
      optionsContainer.querySelectorAll("button").forEach((option) => {
        option.disabled = false;
      });
    }
  });

  nextButton.addEventListener("click", () => {
    if (PraxisQuiz.hasNextQuestion()) {
      PraxisQuiz.nextQuestion();
      renderQuestion();
    } else {
      window.location.href = resultsUrl;
    }
  });

  renderQuestion();
});
