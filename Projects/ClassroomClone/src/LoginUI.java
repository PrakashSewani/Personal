import javax.swing.*;
import java.awt.*;

public class LoginUI {
    private JFrame frame;

    private JPanel navPanel;
    private JLabel lblLogo;
    private JPanel buttonPanel;
    private JButton btnLogin;
    private JButton btnRegister;

    private JPanel loginPanel;
    private JLabel lblEmail;
    private JTextField txtEmail;
    private JLabel lblPassword;
    private JPasswordField txtPassword;
    private JButton btnLog;

    private JPanel imagePanel;
    private JLabel lblImage;

    LoginUI() {
        frame = new JFrame("Learning Management System");
        frame.setSize(1000, 800);
        frame.setLayout(new GridBagLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        initNavBar();
        initLoginPanel();
        initImgPanel();
//        resizeImgPanel();


        frame.setVisible(true);
    }

    private void initNavBar() {
        navPanel = new JPanel(new BorderLayout());
//        navPanel.setSize(-1, 100);
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
        btnLogin = new JButton("Login");
        btnLogin.setEnabled(false);
        buttonPanel.add(btnLogin);
        btnRegister = new JButton("Register");
        buttonPanel.add(btnRegister);
        navPanel.add(buttonPanel, BorderLayout.EAST);

        frame.add(navPanel, c);
    }

    private void initLoginPanel() {
        loginPanel = new JPanel(new GridBagLayout());
        loginPanel.setBackground(new Color(100, 100, 255));

        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 1;
        c.gridy = 1;
        c.weightx = 0.15;
        c.weighty = 0.9;
        c.fill = GridBagConstraints.BOTH;

        GridBagConstraints gbc = new GridBagConstraints();

        gbc.gridx = 0;
        gbc.gridy = 0;
        lblEmail = new JLabel("Email:");
        loginPanel.add(lblEmail, gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        txtEmail = new JTextField();
        txtEmail.setPreferredSize(new Dimension(100, 15));
        loginPanel.add(txtEmail, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        lblPassword = new JLabel("Password:");
        loginPanel.add(lblPassword, gbc);

        gbc.gridx = 1;
        gbc.gridy = 1;
        txtPassword = new JPasswordField();
        txtPassword.setPreferredSize(new Dimension(100, 15));
        loginPanel.add(txtPassword, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = GridBagConstraints.REMAINDER;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.anchor = GridBagConstraints.CENTER;
        btnLog = new JButton("Login");
        loginPanel.add(btnLog, gbc);

        frame.add(loginPanel, c);
    }

    private void initImgPanel() {
        imagePanel = new JPanel(new FlowLayout());
        imagePanel.setBackground(new Color(255, 100, 100));

        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0;
        c.gridy = 1;
        c.weightx = 0.85;
        c.weighty = 0.9;
        c.fill = GridBagConstraints.BOTH;

        String path = RegisterUI.class.getClassLoader().getResource("placeholder.jpg").getPath().replaceAll("%20", " ");
        System.out.println(path);
        Image img = new ImageIcon(path).getImage();
        int panelWidth = imagePanel.getPreferredSize().width;
        lblImage = new JLabel(new ImageIcon(img.getScaledInstance(200, -1, Image.SCALE_DEFAULT)));
        imagePanel.add(lblImage);

        frame.add(imagePanel, c);
    }

    private void resizeImgPanel() {
        int panelWidth = imagePanel.getPreferredSize().width;
        System.out.println(panelWidth);

        ImageIcon icn  = (ImageIcon) lblImage.getIcon();
        Image img = icn.getImage();
        lblImage.setIcon(new ImageIcon(img.getScaledInstance(panelWidth, -1, Image.SCALE_DEFAULT)));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(LoginUI::new);
    }
}
