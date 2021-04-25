import javax.swing.*;
import java.awt.*;

public class HomePageUI {

    private JFrame frame;
    private JPanel navPanel;
    private JPanel MainClassPanel;
    private JPanel Classes;
    private JLabel lblLogo;
    private JPanel buttonPanel;
    private JButton btnCreateClass;
    private JButton btnJoinClass;
    private JLabel lblUser;
    private JButton btnHome;
    private JPanel NoClasses;
    private JPanel YesClasses;
    private JPanel MainAnnouncement;
    private JPanel Announce;
    private JPanel NoAnnounce;
    private JPanel YesAnnounce;
    private JScrollPane FinalClass;
    private JScrollPane FinalAnnouce;

    HomePageUI() {
        frame = new JFrame("Learning Management System");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setLayout(new GridBagLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();

        initNavBar();
        ClassPanel();
        AnnouncementPanel();

        frame.setVisible(true);
    }

    private void initNavBar() {
        navPanel = new JPanel(new BorderLayout());
        navPanel.setSize(-1, 100);
        navPanel.setBackground(new Color(128, 128, 128));

        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0;
        c.gridy = 0;
        c.fill = GridBagConstraints.HORIZONTAL;
        c.gridwidth = GridBagConstraints.REMAINDER;
        c.anchor = GridBagConstraints.FIRST_LINE_START;
//        c.weighty = 0.05;

        lblLogo = new JLabel("Logo");
        navPanel.add(lblLogo, BorderLayout.WEST);

        buttonPanel = new JPanel(new FlowLayout());
        buttonPanel.setOpaque(false);
        btnHome = new JButton("Home");
        buttonPanel.add(btnHome);
        btnJoinClass = new JButton("Join Class");
        buttonPanel.add(btnJoinClass);
        btnCreateClass = new JButton("Create Class");
        buttonPanel.add(btnCreateClass);
        navPanel.add(buttonPanel, BorderLayout.CENTER);

        lblUser = new JLabel("Username");
        navPanel.add(lblUser, BorderLayout.EAST);

        frame.add(navPanel, c);
    }

    private void ClassPanel(){
        MainClassPanel = new JPanel(new GridBagLayout());
        MainClassPanel.setPreferredSize(new Dimension(450,-1));
        MainClassPanel.setBackground(new Color(225,100,100));

        GridBagConstraints d = new GridBagConstraints();
        d.gridx = 0;
        d.gridy = 1;
        d.weightx=0.20;
        d.weighty=0.9;
        d.fill = GridBagConstraints.VERTICAL;
        d.anchor = GridBagConstraints.WEST;

        frame.add(MainClassPanel,d);

        GridBagConstraints abc = new GridBagConstraints();
        abc.gridx = 1;
        abc.gridy = 1;
        abc.weightx = 0.20;
        abc.weighty = 0.90;
        abc.fill = GridBagConstraints.BOTH;

        Classes = new JPanel(new CardLayout());
        Classes.setBackground(new Color(225,100,225));
        MainClassPanel.add(Classes,abc);

        NoClasses = new JPanel(new GridBagLayout());
        NoClasses.setPreferredSize(new Dimension(450,-1));
        NoClasses.setBackground(new Color(100,225,100));

        //Classes.add(NoClasses);

        YesClasses = new JPanel(new GridBagLayout());
        YesClasses.setPreferredSize(new Dimension(450,-1));
        YesClasses.setBackground(new Color(100,100,225));

        FinalClass = new JScrollPane(YesClasses,JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        GridBagConstraints J = new GridBagConstraints();
        J.gridx = 1;
        J.gridy = 1;
        J.fill = GridBagConstraints.VERTICAL;
        J.anchor = GridBagConstraints.WEST;

        YesClasses.add(FinalClass,J);

        Classes.add(YesClasses);

    }

    private void AnnouncementPanel(){
        MainAnnouncement = new JPanel(new GridBagLayout());
        MainAnnouncement.setPreferredSize(new Dimension(1470,-1));
        MainAnnouncement.setBackground(new Color(100,100,225));

        GridBagConstraints d = new GridBagConstraints();
        d.gridx = 0;
        d.gridy = 1;
        d.weightx=0.80;
        d.weighty=0.9;
        d.fill = GridBagConstraints.VERTICAL;
        d.anchor = GridBagConstraints.EAST;

        frame.add(MainAnnouncement,d);

        Announce = new JPanel(new CardLayout());
        Announce.setPreferredSize(new Dimension(1470,-1));
        Announce.setBackground(new Color(100,225,100));

        GridBagConstraints abc = new GridBagConstraints();
        abc.gridx = 0;
        abc.gridy = 1;
        abc.weightx = 0.80;
        abc.weighty = 0.90;
        abc.fill = GridBagConstraints.BOTH;

        MainAnnouncement.add(Announce,abc);

        NoAnnounce = new JPanel(new GridBagLayout());
        NoAnnounce.setPreferredSize(new Dimension(1470,-1));
        NoAnnounce.setBackground(new Color(225,100,225));

        Announce.add(NoAnnounce);

        YesAnnounce = new JPanel(new GridBagLayout());
        YesAnnounce.setPreferredSize(new Dimension(1470,-1));
        YesAnnounce.setBackground(new Color(225,100,100));

        FinalAnnouce = new JScrollPane(YesAnnounce,JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);

        GridBagConstraints J = new GridBagConstraints();
        J.gridx = 1;
        J.gridy = 1;
        J.fill = GridBagConstraints.VERTICAL;
        J.anchor = GridBagConstraints.WEST;

        YesAnnounce.add(FinalAnnouce,J);

        Announce.add(YesAnnounce);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(HomePageUI::new);
    }
}
