class Boggle2 {
  
    constructor(boardId, seconds = 60) {
        this.board = $("#" + boardId);
        this.words = new Set();
        this.score = 0;
        this.seconds = seconds;
        this.showTimer();
        this.timer = setInterval(this.countdown(), 1000);
        $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
    }
    
    showTimer() {
        $(".timer", this.board).text(this.seconds);
    }
    async countDown(){
        this.seconds = this.seconds -1;
        this.showTimer();

        if (this.seconds === 0){
            clearInterval(this.timer);
            await this.scoreGame();
        }
    }
    showMessage(msg, style) {
        $(".msg", this.board)
          .text(msg)
          .removeClass()
          .addClass(`msg ${style}`);
    }
    showScore() {
        $(".score", this.board).text(this.score);
    }
    
    async handleButton(e){
        e.preventDefault();
        const $word = $(".word", this.board);
        let word = $word.val();

        if (this.words.has(word)){
            this.showMessage(`${word} has already been guessed`, "err");
            return;
        }
        if (!word) return;
        
        const resp = await axios.get("/check-word", { params: { word: word }});
        if (resp.data.result === "not-word") {
            this.showMessage(`${word} is not a valid word`, "err");
          } else if (resp.data.result === "not-on-board") {
            this.showMessage(`${word} is not a valid word on this board`, "err");
          } else {
            this.words.add(word);
            this.showMessage(`Added: ${word}`, "ok");
            this.score += word.length;
            this.showScore();
          }
      
          $word.val("");
    }

    async highScore(){
        $(".add-word", this.board).hide();
        const resp = await axios.post("/post-score", { score: this.score });
        if (resp.data.brokeRecord) {
          this.showMessage(`New record: ${this.score}`, "ok");
        } else {
          this.showMessage(`Final score: ${this.score}`, "ok");
        }
    }
    






}