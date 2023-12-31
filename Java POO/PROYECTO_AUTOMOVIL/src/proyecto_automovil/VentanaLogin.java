/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package proyecto_automovil;

import java.awt.Image;
import java.awt.Toolkit;
import java.sql.*;

/**
 *
 * @author SkyHell
 */
public class VentanaLogin extends javax.swing.JFrame {

    VentanaPrincipal vp= new VentanaPrincipal();

    /**
     * Creates new form VentanaLogin
     */
    @Override
    public Image getIconImage(){
        Image reValue= Toolkit.getDefaultToolkit().getImage(ClassLoader.getSystemResource("imagenes/icons8-business-48.png"));
        return reValue;
    }
    
    public VentanaLogin() {
        initComponents();
        setLocationRelativeTo(null);
        setTitle("LOGIN");
        setResizable(false);
        setIconImage(getIconImage());
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        LogoFondo = new javax.swing.JLabel();
        inicioSesionLogo = new javax.swing.JLabel();
        logoUsuario = new javax.swing.JLabel();
        ingresoUsuario = new javax.swing.JTextField();
        jLabel1 = new javax.swing.JLabel();
        ingresoContraseña = new javax.swing.JPasswordField();
        botonIngresar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel1.setBackground(new java.awt.Color(1, 1, 1));

        LogoFondo.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        LogoFondo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/Logo.jpg"))); // NOI18N

        inicioSesionLogo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/letra.png"))); // NOI18N

        logoUsuario.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/logoUsuario.png"))); // NOI18N

        ingresoUsuario.setBackground(new java.awt.Color(102, 102, 102));
        ingresoUsuario.setFont(new java.awt.Font("MS Reference Sans Serif", 0, 14)); // NOI18N
        ingresoUsuario.setForeground(new java.awt.Color(255, 255, 255));

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/logoContraseña.png"))); // NOI18N

        ingresoContraseña.setBackground(new java.awt.Color(102, 102, 102));
        ingresoContraseña.setForeground(new java.awt.Color(255, 255, 255));
        ingresoContraseña.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ingresoContraseñaActionPerformed(evt);
            }
        });

        botonIngresar.setBackground(new java.awt.Color(102, 102, 102));
        botonIngresar.setText("INGRESAR");
        botonIngresar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                botonIngresarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(0, 184, Short.MAX_VALUE)
                .addComponent(LogoFondo)
                .addGap(156, 156, 156))
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(291, 291, 291)
                        .addComponent(inicioSesionLogo))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(350, 350, 350)
                        .addComponent(logoUsuario))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(348, 348, 348)
                        .addComponent(botonIngresar))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(328, 328, 328)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(ingresoContraseña, javax.swing.GroupLayout.PREFERRED_SIZE, 124, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel1)
                            .addComponent(ingresoUsuario, javax.swing.GroupLayout.PREFERRED_SIZE, 124, javax.swing.GroupLayout.PREFERRED_SIZE))))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(17, 17, 17)
                .addComponent(inicioSesionLogo)
                .addGap(44, 44, 44)
                .addComponent(logoUsuario)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(ingresoUsuario, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jLabel1)
                .addGap(18, 18, 18)
                .addComponent(ingresoContraseña, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(botonIngresar)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 33, Short.MAX_VALUE)
                .addComponent(LogoFondo, javax.swing.GroupLayout.PREFERRED_SIZE, 97, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 807, -1));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void ingresoContraseñaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ingresoContraseñaActionPerformed

    }//GEN-LAST:event_ingresoContraseñaActionPerformed

    private void botonIngresarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_botonIngresarActionPerformed
        String usuario = ingresoUsuario.getText();
        String contraseña = ingresoContraseña.getText();

        try {

            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/proyecto_automovil", "root", "");
            Statement st = conexion.createStatement();

            ResultSet rs = st.executeQuery("select * from usuario");

            while (rs.next()) {
                if (rs.getString("username").equals(usuario)) {
                    if (rs.getString("password").equals(contraseña)) {
                        dispose();
                        vp.setVisible(true);
                        break;
                    }
                    break;
                }
            }

        } catch (Exception e) {
        }
    }//GEN-LAST:event_botonIngresarActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(VentanaLogin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(VentanaLogin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(VentanaLogin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(VentanaLogin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new VentanaLogin().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel LogoFondo;
    private javax.swing.JButton botonIngresar;
    private javax.swing.JPasswordField ingresoContraseña;
    private javax.swing.JTextField ingresoUsuario;
    private javax.swing.JLabel inicioSesionLogo;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JLabel logoUsuario;
    // End of variables declaration//GEN-END:variables


}
