package lab1;
import java.util.Arrays;
public abstract class Monster {
	protected String type;
	protected int hitPoints;
	protected int attackPoints;
	protected String[] weaknesses;

	public Monster(String type,int hitPoints, int attackPoints, String[] weaknesses) {
		this.type=type;
		this.hitPoints=hitPoints;
		this.attackPoints=attackPoints;
		this.weaknesses=weaknesses;
	}
	//getters
	public int getHitPoints() {
		return this.hitPoints;
	}
	public int getAttackPoints() {
		return this.attackPoints;
	}
	public String getType() {
		return this.type;
	}
	//the required functions
	public boolean isWeakAgainst(String otherType) {
		for(String weak: this.weaknesses) {
			if(weak.equals(otherType)) {
				return true;
			}
		}
		return false;
	}
	public void removeHitPoints(int pointsToRemove) {
		if(this.hitPoints-pointsToRemove>0) {
			this.hitPoints-=pointsToRemove;
		}else {
			this.hitPoints=0;
		}
		
	}
	public boolean attack(Monster otherMonster) {
		if(otherMonster==this) {
			return false;
		}
		if(this.hitPoints<=0||otherMonster.getHitPoints()<=0) {
			return false;
		}
		boolean otherIsWeak=otherMonster.isWeakAgainst(type);
		int pointsToRemove = (otherIsWeak) ? this.attackPoints + 20: this.attackPoints;
		otherMonster.removeHitPoints(pointsToRemove);
		return true;

	}
	public abstract boolean dodge();
	
	@Override
	public String toString() {
		return "Monster [type=" + type + ", hitPoints=" + hitPoints+ ", attackPoints=" + attackPoints + ", weaknesses="+ Arrays.toString(weaknesses) + "]";
	}
//	public static void main(String[] args) {
//		Monster fireMonster = new Monster("Fire", 200, 100, new String[] { "Water" });
//		Monster waterMonster = new Monster("Water", 130, 50, new String[] { "Fire", "Electric" });
//		waterMonster.attack(fireMonster); // Should return true
//		System.out.println(fireMonster.getHitPoints()); // ShouldprintfireMonster.getHitPoints();
//	}
	
	public static class WaterMonster extends Monster {
		public WaterMonster(int hitPoints, int attackPoints) {
		super("Water", hitPoints, attackPoints, new String[] { "Fire",
		"Electric" } );
		}
		@Override
		public boolean dodge() {
		return (hitPoints >= 100);
		}
		}
		public static class FireMonster extends Monster {
		private boolean lastDodge = false;
		public FireMonster(int hitPoints, int attackPoints) {
		super("Fire", hitPoints, attackPoints, new String[] { "Water" });
		}
		@Override
		public boolean dodge() {
		return (lastDodge = !lastDodge);
		}
		}
		public class ElectricMonster extends Monster {
		public ElectricMonster(int hitPoints, int attackPoints) {
		super("Electric", hitPoints, attackPoints, new String[0]);
		}
		@Override
		public boolean dodge() {
		return false;
		}
		}
		public static void main(String[] args) {
		FireMonster fireMonster =new FireMonster(200,100);
		WaterMonster waterMonster = new WaterMonster(130, 50);
		waterMonster.attack(fireMonster); // Should return true
		System.out.println(fireMonster.getHitPoints()); // ShouldprintfireMonster.getHitPoints();
	}
}
