package com.example.onroadvehiclebreakdown;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Usersendrequest extends AppCompatActivity implements JsonResponse{
    EditText e1;
    String problem;
    Button b1;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usersendrequest);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        e1=(EditText)findViewById(R.id.etcomplaint);
        b1=(Button)findViewById(R.id.button);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                problem=e1.getText().toString();
                   if(problem.equalsIgnoreCase("")|| !problem.matches("[a-zA-Z ]+"))
                {
                    e1.setError("Enter your problem");
                    e1.setFocusable(true);
                }
                   else {
                       JsonReq JR = new JsonReq();
                       JR.json_response = (JsonResponse) Usersendrequest.this;
                       String q = "/usersendrequest?problem=" + problem + "&lid=" + sh.getString("log_id", "") + "&mid=" + Userviewmearestmechanic.mids;
                       q = q.replace(" ", "%20");
                       JR.execute(q);
                   }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {


                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "SENDED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getApplicationContext(), Usersendrequest.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }


        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
}