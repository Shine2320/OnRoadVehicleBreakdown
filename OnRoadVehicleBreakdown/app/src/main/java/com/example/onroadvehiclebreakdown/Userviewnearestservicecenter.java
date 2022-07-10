package com.example.onroadvehiclebreakdown;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userviewnearestservicecenter extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {

    ListView l1;
    String[] shopname,latitude,longitude,place,phone,email,value;
    public static String lati,longi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewnearestservicecenter);

        startService(new Intent(getApplicationContext(),LocationService.class));

        l1=(ListView)findViewById(R.id.lvview);
        l1.setOnItemClickListener(this);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Userviewnearestservicecenter.this;
        String q="/userviewnearestservicecenter?lati="+LocationService.lati+"&longi="+LocationService.logi;
        q=q.replace(" ","%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status=jo.getString("status");
            Log.d("pearl",status);


            if(status.equalsIgnoreCase("success")){
                JSONArray ja1=(JSONArray)jo.getJSONArray("data");
                shopname=new String[ja1.length()];
                latitude=new String[ja1.length()];
                longitude=new String[ja1.length()];
                place=new String[ja1.length()];
                phone=new String[ja1.length()];
                email=new String[ja1.length()];

                value=new String[ja1.length()];

                for(int i = 0;i<ja1.length();i++)
                {
                    shopname[i]=ja1.getJSONObject(i).getString("centername");
                    latitude[i]=ja1.getJSONObject(i).getString("latitude");
                    longitude[i]=ja1.getJSONObject(i).getString("longitude");
                    place[i]=ja1.getJSONObject(i).getString("place");
                    phone[i]=ja1.getJSONObject(i).getString("phone");
                    email[i]=ja1.getJSONObject(i).getString("email");
                    value[i]="Center Name: "+shopname[i]+"\nPlace: "+place[i]+"\nPhone: "+phone[i]+"\nEmail: "+email[i]+"\nLatitude: "+latitude[i]+"\nLongitude: "+longitude[i];

                }
                ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,value);
                l1.setAdapter(ar);
            }


        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        lati=latitude[position];
        longi=longitude[position];
        final CharSequence[] items = {"MAP","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(Userviewnearestservicecenter.this);
        // builder.setTitle("Add Photo!");
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("MAP")) {

                    String url = "http://www.google.com/maps?q=" + lati + "," + longi;
                    Intent in = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                    startActivity(in);
                }

                else if (items[item].equals("Cancel")) {
                    dialog.dismiss();
                }
            }

        });
        builder.show();
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
}