import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Register {
    private JPanel RegisterPanel;
    private JPanel ImagePanel;
    private JPanel ProjectNamePanel;
    private JPanel ButtonsPanel;
    private JTextField fNamefield;
    private JTextField eMailfield;
    private JPasswordField pAsswordfield;
    private JButton registerButton;
    private JLabel fname;
    private JLabel eMail;
    private JLabel pAssword;
    private JLabel pRojectnAme;
    private JButton MainLogin;
    private JButton MainRegister;
    private JLabel Join;

    public Register() {
        registerButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
        MainLogin.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
        MainRegister.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
    }
}
