package com.example.onroadvehiclebreakdown;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Usereditprofile extends AppCompatActivity implements JsonResponse {
    EditText e1,e2,e3,e4,e5;
    Button b1;
    String fname,lname,place,phone,email;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usereditprofile);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.etupfname);
        e2=(EditText)findViewById(R.id.etuplname);
        e3=(EditText)findViewById(R.id.etupplace);
        e4=(EditText)findViewById(R.id.etupphone);
        e5=(EditText)findViewById(R.id.etupemail);
        b1=(Button)findViewById(R.id.button17);
        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse) Usereditprofile.this;
        String q = "/userview?lid="+sh.getString("log_id","");
        q=q.replace(" ","%20");
        JR.execute(q);
        startService(new Intent(getApplicationContext(),LocationService.class));
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                fname=e1.getText().toString();
                lname=e2.getText().toString();
                place=e3.getText().toString();
                phone=e4.getText().toString();
                email=e5.getText().toString();
                if(fname.equalsIgnoreCase("")|| !fname.matches("[a-zA-Z ]+"))
                {
                    e1.setError("Enter your First name");
                    e1.setFocusable(true);
                }
                else if(lname.equalsIgnoreCase("")|| !place.matches("[a-zA-Z ]+"))
                {
                    e2.setError("Enter your Last name");
                    e2.setFocusable(true);
                }

                else if(place.equalsIgnoreCase("")|| !place.matches("[a-zA-Z ]+"))
                {
                    e3.setError("Enter your place");
                    e3.setFocusable(true);
                }
                else if(phone.equalsIgnoreCase("") || phone.length()!=10)
                {
                    e4.setError("Enter your phone no.");
                    e4.setFocusable(true);
                }
                else if(email.equalsIgnoreCase("") || !email.matches("[a-zA-Z0-9._-]+@[a-z]+\\.[a-z]+"))
                {
                    e5.setError("Enter your email");
                    e5.setFocusable(true);
                }
                else {
                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) Usereditprofile.this;
                    String q = "/userupdate?lid=" + sh.getString("log_id", "") +"&fname="+fname+"&lname="+lname+ "&place=" + place + "&phone=" + phone + "&email=" + email + "&latitude=" + LocationService.lati + "&longitude=" + LocationService.logi;
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
try{
        String method = jo.getString("method");
        if (method.equalsIgnoreCase("userupdate")) {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), "UPDATED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Userhome.class));

            } else {

                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
            }
        } else if (method.equalsIgnoreCase("userview")) {
            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");

                e1.setText(ja1.getJSONObject(0).getString("firstname"));
                e2.setText(ja1.getJSONObject(0).getString("lastname"));
                e3.setText(ja1.getJSONObject(0).getString("place"));
                e4.setText(ja1.getJSONObject(0).getString("phone"));
                e5.setText(ja1.getJSONObject(0).getString("email"));
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
        Intent b = new Intent(getApplicationContext(), Userhome.class);
        startActivity(b);
    }
}