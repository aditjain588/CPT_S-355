import java.awt.Color;

public class player {

	int score;
	int hits;
	int hitBasic;
	int hitShrink;
	int hitBounce;
	int hitSplit;
	
	public player()
	{
		score=0;
		hits=0;
	}
	
	int updatescore(int plus)
	{
		score+=plus;
		return score;
	}
	int getScore()
	{
		return score;
	}
	
	int updateHits()
	{
		hits+=1;
		return hits;
	}
	int getnumHits()
	{
		return hits;
	}
	void updatehitBounce()
	{
		hitBounce++;
	}
	int gethitBounce()
	{
		return hitBounce;
	}
	void updatehitShrink()
	{
		hitShrink++;
	}
	int gethitShrink()
	{
		return hitShrink;
	}
	void updatehitBasic()
	{
		hitBasic++;
	}
	int gethitBasic()
	{
		return hitBasic;
	}
	void updatehitSplit()
	{
		hitSplit++;
	}
	int gethitSplit()
	{
		return hitSplit;
	}
	public String mosthits()
	{
		
		int mostBallHit = Math.max(Math.max(hitBasic,hitSplit), Math.max(hitBounce, hitShrink));
		if(mostBallHit==hitBounce) {
			return "Bounce Ball";
		}
		else if(mostBallHit==hitBasic) {
			return "Basic Ball";
		}
		else if(mostBallHit==hitShrink) {
			return "Shrink Ball";
		}	
		else if(mostBallHit==hitSplit) {
			return "Split Ball";
		}
		return null;
		}
}

