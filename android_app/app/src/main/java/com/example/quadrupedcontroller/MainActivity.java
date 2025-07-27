package com.example.quadrupedcontroller;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.TextView;
import java.io.OutputStream;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {

    private TextView linearVelocityTextView;
    private TextView angularVelocityTextView;
    private FrameLayout leftJoystick;
    private FrameLayout rightJoystick;

    private Socket socket;
    private OutputStream outputStream;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        linearVelocityTextView = findViewById(R.id.linearVelocityTextView);
        angularVelocityTextView = findViewById(R.id.angularVelocityTextView);
        leftJoystick = findViewById(R.id.leftJoystick);
        rightJoystick = findViewById(R.id.rightJoystick);

        setupJoysticks();
        connectToRobot();
    }

    private void setupJoysticks() {
        leftJoystick.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                float x = event.getX() / v.getWidth();
                float y = event.getY() / v.getHeight();
                updateLinearVelocity(y);
                return true;
            }
        });

        rightJoystick.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                float x = event.getX() / v.getWidth();
                updateAngularVelocity(x);
                return true;
            }
        });
    }

    private void updateLinearVelocity(float value) {
        linearVelocityTextView.setText(String.format("%.2f", value));
        sendCommand("linear_velocity", value);
    }

    private void updateAngularVelocity(float value) {
        angularVelocityTextView.setText(String.format("%.2f", value));
        sendCommand("angular_velocity", value);
    }

    private void connectToRobot() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    socket = new Socket("192.168.1.100", 12345); // Replace with your robot's IP address
                    outputStream = socket.getOutputStream();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }

    private void sendCommand(String command, float value) {
        if (outputStream != null) {
            try {
                String message = command + ":" + value + "\n";
                outputStream.write(message.getBytes());
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        try {
            if (socket != null) {
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}