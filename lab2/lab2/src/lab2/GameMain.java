package lab2;

public class GameMain {
	public enum GameResult {
		WIN,
		LOSE,
		DRAW;
	}
	public enum Symbol {
		 ROCK,
		 PAPER,
		 SCISSORS;

		public GameResult getResul(Symbol s) {
			if (this.equals(s)){
				return GameResult.DRAW;
			}
			switch(this) {
				case ROCK:
					if(s==PAPER) {
						return GameResult.LOSE;
					}else {
						return GameResult.WIN;
					}
				case PAPER:
					if(s==SCISSORS) {
						return GameResult.LOSE;
					}else {
						return GameResult.WIN;
					}
				case SCISSORS:
					if(s==ROCK) {
						return GameResult.LOSE;
					}else {
						return GameResult.WIN;
					}
				default:
					return null;
				}
			
			
			
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
