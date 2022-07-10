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

public class Mechaniceditprofile extends AppCompatActivity implements JsonResponse{
    EditText e1,e2,e3,e4;
    Button b1;
    String fname,place,phone,email;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mechaniceditprofile);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        startService(new Intent(getApplicationContext(),LocationService.class));
        e1=(EditText)findViewById(R.id.etfname);

//        e2=(EditText)findViewById(R.id.etlname);

        e2=(EditText)findViewById(R.id.etplace);
        e3=(EditText)findViewById(R.id.etphone);
        e4=(EditText)findViewById(R.id.etemail);
//        e8=(EditText)findViewById(R.id.etuser);
//        e9=(EditText)findViewById(R.id.etpass);
        b1=(Button)findViewById(R.id.button);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Mechaniceditprofile.this;
        String q="/mechanicviewprofile?lid="+sh.getString("log_id","");
        q=q.replace(" ","%20");
        JR.execute(q);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                fname=e1.getText().toString();
                place=e2.getText().toString();
                phone=e3.getText().toString();
                email=e4.getText().toString();


                if(fname.equalsIgnoreCase("")|| !fname.matches("[a-zA-Z ]+"))
                {
                    e1.setError("Enter your Shopname");
                    e1.setFocusable(true);
                }


                else if(place.equalsIgnoreCase(""))
                {
                    e2.setError("Enter your place");
                    e2.setFocusable(true);
                }
                else if(phone.equalsIgnoreCase("") || phone.length()!=10)
                {
                    e3.setError("Enter your phone no.");
                    e3.setFocusable(true);
                }
                else if(email.equalsIgnoreCase("") || !email.matches("[a-zA-Z0-9._-]+@[a-z]+\\.[a-z]+"))
                {
                    e4.setError("Enter your email");
                    e4.setFocusable(true);
                }
                else {
                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) Mechaniceditprofile.this;
                    String q = "/mechaniceditprofile?lid=" + sh.getString("log_id", "") + "&name=" + fname + "&place=" + place + "&phone=" + phone + "&email=" + email + "&latitude=" + LocationService.lati + "&longitude=" + LocationService.logi;
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {

            String method = jo.getString("method");
            if (method.equalsIgnoreCase("mechaniceditprofile")) {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "UPDATED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getApplicationContext(), Mechanichome.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }
            } else if (method.equalsIgnoreCase("mechanicviewprofile")) {
                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    JSONArray ja1 = (JSONArray) jo.getJSONArray("data");

                    e1.setText(ja1.getJSONObject(0).getString("shopname"));
                    e2.setText(ja1.getJSONObject(0).getString("place"));
                    e3.setText(ja1.getJSONObject(0).getString("phone"));
                    e4.setText(ja1.getJSONObject(0).getString("email"));
//                    reply[i] = ja1.getJSONObject(i).getString("reply");
//                    date[i] = ja1.getJSONObject(i).getString("date");

                }
            }

        }

        catch(Exception e){
                // TODO: handle exception
                e.printStackTrace();
                Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
            }

    }

        public void onBackPressed ()
        {
            // TODO Auto-generated method stub
            super.onBackPressed();
            Intent b = new Intent(getApplicationContext(), Mechanichome.class);
            startActivity(b);
        }
    }