public class OldRobotBuilder implements RobotBuilder{
    private Robot robot;

    public OldRobotBuilder(){
        this.robot = new Robot();
    }
    @Override
    public void buildRobotHead() {
        this.robot.setRobotHead("Tin Head");
    }

    @Override
    public void buildRobotTorso() {
        this.robot.setRobotTorso("Tin Torso");

    }

    @Override
    public void buildRobotArms() {
        this.robot.setRobotArms("Blowtorch Arms");

    }

    @Override
    public void buildRobotLegs() {
        this.robot.setRobotLegs("Rollar skates");

    }

    @Override
    public Robot getRobot() {
        return this.robot;
    }
}
