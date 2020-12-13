import java.awt.Color;

public class Bounce extends Basic{
	int bounceCount=3;
	public Bounce(double r, Color c) {
	       super(r,c);
	       
	    }
	public int reset() {
        rx = 0.0;
        ry = 0.0;  	
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        return 2;
    }
	public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) {
        	bounceCount--;
        	if(bounceCount==0) {
        	isOut = true;
        	}
        	else {
        		if(Math.abs(rx) > 1.0) {
        			vx=-vx;
        			rx=rx+vx;
        		}
        		else {
        			vy=-vy;
        			ry=ry+vy;
        		}
        		}
        	}
	}   
	
	public int getScore() {
    	return 15;
    }
}
