/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package proyecto_automovil;

import java.awt.Color;
import java.awt.Image;
import java.awt.Toolkit;
import java.sql.*;

/**
 *
 * @author SkyHell
 */
public class VentanaPrincipal extends javax.swing.JFrame {

    VentanaIngresoAuto via= new VentanaIngresoAuto();
    VentanaIngresoCamion vic= new VentanaIngresoCamion();
    VentanaModificarAuto vm= new VentanaModificarAuto();
    
    /**
     * Creates new form VentanaLogin
     */
    
        @Override
    public Image getIconImage(){
        Image reValue= Toolkit.getDefaultToolkit().getImage(ClassLoader.getSystemResource("imagenes/icons8-business-48.png"));
        return reValue;
    }
    
    public VentanaPrincipal() {
        initComponents();
        setLocationRelativeTo(null);
        setTitle("LOGIN");
        setResizable(false);
        jMenuBar1.setBackground(Color.GRAY);
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
        jMenuBar1 = new javax.swing.JMenuBar();
        opcionIngreso = new javax.swing.JMenu();
        IngresoAuto = new javax.swing.JMenuItem();
        ingresoCamion = new javax.swing.JMenuItem();
        opcionModificar = new javax.swing.JMenu();
        modificarAuto = new javax.swing.JMenuItem();
        modificarCamion = new javax.swing.JMenuItem();
        jMenu3 = new javax.swing.JMenu();
        jMenu4 = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel1.setBackground(new java.awt.Color(1, 1, 1));

        LogoFondo.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        LogoFondo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/Logo.jpg"))); // NOI18N

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(0, 184, Short.MAX_VALUE)
                .addComponent(LogoFondo)
                .addGap(156, 156, 156))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap(317, Short.MAX_VALUE)
                .addComponent(LogoFondo, javax.swing.GroupLayout.PREFERRED_SIZE, 97, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 807, 420));

        jMenuBar1.setBackground(new java.awt.Color(102, 102, 102));
        jMenuBar1.setBorder(null);

        opcionIngreso.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/ingresarLogo.png"))); // NOI18N

        IngresoAuto.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_A, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        IngresoAuto.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/autoLogo.png"))); // NOI18N
        IngresoAuto.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                IngresoAutoActionPerformed(evt);
            }
        });
        opcionIngreso.add(IngresoAuto);

        ingresoCamion.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_S, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        ingresoCamion.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/camionLogo.png"))); // NOI18N
        ingresoCamion.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ingresoCamionActionPerformed(evt);
            }
        });
        opcionIngreso.add(ingresoCamion);

        jMenuBar1.add(opcionIngreso);

        opcionModificar.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/modificarLogo.png"))); // NOI18N
        opcionModificar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                opcionModificarActionPerformed(evt);
            }
        });

        modificarAuto.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_A, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        modificarAuto.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/autoLogo.png"))); // NOI18N
        modificarAuto.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                modificarAutoActionPerformed(evt);
            }
        });
        opcionModificar.add(modificarAuto);

        modificarCamion.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_S, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        modificarCamion.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/camionLogo.png"))); // NOI18N
        modificarCamion.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                modificarCamionActionPerformed(evt);
            }
        });
        opcionModificar.add(modificarCamion);

        jMenuBar1.add(opcionModificar);

        jMenu3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/eliminarLogo.png"))); // NOI18N
        jMenuBar1.add(jMenu3);

        jMenu4.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagenes/mostrarLogo.png"))); // NOI18N
        jMenuBar1.add(jMenu4);

        setJMenuBar(jMenuBar1);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void IngresoAutoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_IngresoAutoActionPerformed
        dispose();
        via.setVisible(true);
    }//GEN-LAST:event_IngresoAutoActionPerformed

    private void ingresoCamionActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ingresoCamionActionPerformed
        dispose();
        vic.setVisible(true);
    }//GEN-LAST:event_ingresoCamionActionPerformed

    private void opcionModificarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_opcionModificarActionPerformed

    }//GEN-LAST:event_opcionModificarActionPerformed

    private void modificarAutoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_modificarAutoActionPerformed
        dispose();
        VentanaModificarAuto vma= new VentanaModificarAuto();
        vma.setVisible(true);
    }//GEN-LAST:event_modificarAutoActionPerformed

    private void modificarCamionActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_modificarCamionActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_modificarCamionActionPerformed

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
    private javax.swing.JMenuItem IngresoAuto;
    private javax.swing.JLabel LogoFondo;
    private javax.swing.JMenuItem ingresoCamion;
    private javax.swing.JMenu jMenu3;
    private javax.swing.JMenu jMenu4;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JMenuItem modificarAuto;
    private javax.swing.JMenuItem modificarCamion;
    private javax.swing.JMenu opcionIngreso;
    private javax.swing.JMenu opcionModificar;
    // End of variables declaration//GEN-END:variables
}