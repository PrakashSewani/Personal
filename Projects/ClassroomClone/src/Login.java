import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Login {
    private JPasswordField pAsswordfield;
    private JTextField eMailfield;
    private JButton LoginButton;
    private JButton MainRegister;
    private JButton MainLogin;
    private JPanel NavBarPanel;
    private JPanel ProjectNamePanel;
    private JLabel ProjectName;
    private JPanel ButtonPanel;
    private JPanel ImagePanel;
    private JPanel LoginPanel;
    private JPanel Login;
    private JLabel LoginLabel;
    private JLabel eMail;
    private JLabel pAssword;

    public Login() {
        MainRegister.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
        LoginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
        MainLogin.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
    }
}
