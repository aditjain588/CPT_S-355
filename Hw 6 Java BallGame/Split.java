import java.awt.Color;

public class Split extends Basic {
	public Split(double r, Color c) {
	       super(r,c);
	    }
	public int reset() {
        rx = 0.0;
        ry = 0.0;  	
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        return 4;
    }
	public int getScore() {
    	return 10;
    }
}
