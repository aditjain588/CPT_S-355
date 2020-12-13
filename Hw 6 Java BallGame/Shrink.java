import java.awt.Color;

public class Shrink extends Basic{
	double origRad;
	public Shrink(double r, Color c) {
       super(r,c);
       origRad=radius;
    }
	
	
	public int reset() {
		rx = 0.0;
        ry = 0.0;  	
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        
        if(radius<0.25*origRad) {
        	radius=origRad;
        }
        else {
        radius=radius*0.66;
        }
        return 3;
	}
	public int getScore() {
    	return 20;
    }
}
