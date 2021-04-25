import javax.swing.*;
import java.awt.*;

public class CreateClassUI {

    private JFrame frame;
    private JPanel MainPanel;

    private JLabel CreateClass;
    private JLabel ClassDescriptionField;
    private JTextField ClassName;
    private JTextField ClassCode;
    private JTextField ClassDescription;
    private JButton CreateAClass;

    CreateClassUI(){
        frame = new JFrame("Create a new Classroom");
        frame.setPreferredSize(new Dimension(500,500));
        frame.setLayout(new GridBagLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();

        ClassUI();

        frame.setVisible(true);
    }

    private void ClassUI(){
        MainPanel = new JPanel(new GridBagLayout());
        MainPanel.setBackground(new Color(100,225,100));

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

        CreateClass = new JLabel("Enter ClassName:");
        MainPanel.add(CreateClass,abc);

        GridBagConstraints abc2 = new GridBagConstraints();
        abc2.gridx = 1;
        abc2.gridy = 0;

        ClassName = new JTextField();
        ClassName.setPreferredSize(new Dimension(150,25));
        MainPanel.add(ClassName,abc2);

        GridBagConstraints abc6 = new GridBagConstraints();
        abc6.gridx = 0;
        abc6.gridy = 2;
        abc6.anchor = GridBagConstraints.WEST;

        ClassDescriptionField = new JLabel("Class Description");
        MainPanel.add(ClassDescriptionField,abc6);

        GridBagConstraints abc3 = new GridBagConstraints();
        abc3.gridx = 1;
        abc3.gridy = 2;

        ClassDescription = new JTextField();
        ClassDescription.setPreferredSize(new Dimension(150,150));
        MainPanel.add(ClassDescription,abc3);

        GridBagConstraints abc7 = new GridBagConstraints();
        abc7.gridx = 0;
        abc7.gridy = 3;

        ClassDescriptionField = new JLabel("Class Code for Students");
        MainPanel.add(ClassDescriptionField,abc7);

        GridBagConstraints abc4 = new GridBagConstraints();
        abc4.gridx = 1;
        abc4.gridy = 3;

        ClassCode = new JTextField();
        ClassCode.setPreferredSize(new Dimension(150,25));
        MainPanel.add(ClassCode,abc4);

        GridBagConstraints abc5 = new GridBagConstraints();
        abc5.gridx = 1;
        abc5.gridy = 5;
        abc5.anchor = GridBagConstraints.CENTER;

        CreateAClass = new JButton("Create Classroom");

        MainPanel.add(CreateAClass,abc5);

        frame.add(MainPanel,c);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(CreateClassUI::new);
    }

}
