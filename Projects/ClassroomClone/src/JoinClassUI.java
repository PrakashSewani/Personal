import javax.swing.*;
import java.awt.*;

public class JoinClassUI {

    private JFrame frame;
    private JPanel JoinClass;
    private JLabel JoinText;
    private JTextField Classcode;
    private JButton JoinButton;

    JoinClassUI(){
        frame = new JFrame("Join a Classroom");
        frame.setPreferredSize(new Dimension(500,500));
        frame.setLayout(new GridBagLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();

        JoinAClassUI();

        frame.setVisible(true);
    }

    private void JoinAClassUI(){
        JoinClass = new JPanel(new GridBagLayout());
        JoinClass.setBackground(new Color(100,225,100));

        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0;
        c.gridy = 0;
        c.weightx = 1;
        c.weighty = 1;
        c.fill = GridBagConstraints.BOTH;

        GridBagConstraints abc = new GridBagConstraints();
        abc.gridx = 0;
        abc.gridy = 0;
        abc.anchor = GridBagConstraints.WEST;

        JoinText = new JLabel("Enter Classroom Code");

        JoinClass.add(JoinText,abc);

        GridBagConstraints abc2 = new GridBagConstraints();
        abc2.gridx = 0;
        abc2.gridy = 1;
        abc2.anchor = GridBagConstraints.CENTER;

        Classcode = new JTextField();
        Classcode.setPreferredSize(new Dimension(100,24));

        JoinClass.add(Classcode,abc2);

        GridBagConstraints abc3 = new GridBagConstraints();
        abc3.gridx = 0;
        abc3.gridy = 2;
        abc3.anchor = GridBagConstraints.CENTER;

        JoinButton = new JButton("Join Classroom!");

        JoinClass.add(JoinButton,abc3);

        frame.add(JoinClass,c);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(JoinClassUI::new);
    }
}
