/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: Basic.java StdDraw.java
 *
 *  Creates a Basic ball and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;
import java.util.Arrays; 


public class BallGame { 

    public static void main(String[] args) {
        
    	// number of bouncing balls
        int numBalls =0 ;  
    	try {
            numBalls = Integer.parseInt(args[0]);
        } catch (Exception e) {
            System.out.print("Invalid program argument! - java <num> <type> <radius>\n");

        }
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	
        try {
            //retrieve ball types
            int index =1;
            for (int i=0; i<numBalls; i++) {
                ballTypes[i] = args[index];
                index = index+2;
    	}
        } catch (Exception e) {
            System.out.print("Invalid program argument! - java <num> <type> <radius>\n");
        }

        try {
            //retrieve ball sizes
            int index = 2;
            for (int i=0; i<numBalls; i++) {
                ballSizes[i] = Double.parseDouble(args[index]);
                index = index+2;
    	    }   
        } catch (Exception e) {
            System.out.print("Invalid program argument! - java <num> <type> <radius>\n");
        }
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	player p1=new player();
        p1.hits=0;
        p1.score=0;
        p1.hitBasic=0;
    	p1.hitShrink=0;
    	p1.hitBounce=0;
    	p1.hitSplit=0;
        
    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);
  
        
       
        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
        ArrayList <Basic> ball_list=new ArrayList<Basic>();
        //Basic ball = new Basic(ballSizes[0],Color.RED);
        
        for(int z=0;z<ballTypes.length;z++)
        {
        	if(ballTypes[z].matches("basic")){
        		ball_list.add(new Basic(ballSizes[z],Color.RED));
        	}
        	else if(ballTypes[z].matches("bounce")){
        		ball_list.add(new Bounce(ballSizes[z],Color.BLUE));
        	}
        	else if(ballTypes[z].matches("shrink")){
        		ball_list.add(new Shrink(ballSizes[z],Color.GREEN));
        	}
        	else if(ballTypes[z].matches("split")){
        		ball_list.add(new Split(ballSizes[z],Color.YELLOW));
        	}
        	
        	numBallsinGame++; 
       }
   		//TO DO: initialize the numBallsinGame
   		System.out.println("num balls "+numBallsinGame);
		double rr;
		int res;
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {
        	// TODO: move all balls
        	for(int j=0;j<ball_list.size();j++) {
        	ball_list.get(j).move();
        	}
            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball. 
                for(int j=0;j<ball_list.size();j++) {
                if (ball_list.get(j).isHit(x,y)) {
                		p1.updateHits();
                		res=ball_list.get(j).reset();
                		if(res==2) {
                			p1.updatescore(ball_list.get(j).getScore());
                			p1.updatehitBounce();
                		}
                		else if(res==1) {
                			p1.updatescore(ball_list.get(j).getScore());
                			p1.updatehitBasic();
                		}
                		else if(res==3) {
                			p1.updatescore(ball_list.get(j).getScore());
                			p1.updatehitShrink();
                		}
                		else if (res==4) {
                			rr=ball_list.get(j).radius;
                			p1.updatescore(ball_list.get(j).getScore());
                			p1.updatehitSplit();
                			ball_list.add(new Split(rr,Color.YELLOW));
                			numBallsinGame++;
                		}
                	
                	}  
                
                }
             
                
                	//TO DO: Update player statistics
            }
                   
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game. 
            for(int j=0;j<ball_list.size();j++) {
            if (ball_list.get(j).isOut == false) { 
            	ball_list.get(j).draw();
                numBallsinGame++;
            }
            }
            
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            StdDraw.text(-0.65, 0.85, "Number of hits: "+ Integer.valueOf(p1.getnumHits()));
            StdDraw.text(-0.65, 0.80, "Total score: "+ Integer.valueOf(p1.getScore()));
            
            //TO DO: print the rest of the player statistics
            

            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            StdDraw.text(0, -0.2, "Most hit ball: "+String.valueOf(p1.mosthits()));
            StdDraw.text(0, -0.4, "Total player score: "+String.valueOf(p1.getScore()));
            //TO DO: print the rest of the player statistics
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
