package com.example.onroadvehiclebreakdown;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userviewrequest extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    SharedPreferences sh;
    String[] shopname,problem,amount,date,statuss,rid,value;
    public static String rids,stat,amounts;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewrequest);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        l1=(ListView)findViewById(R.id.lvview);
        l1.setOnItemClickListener(this);

        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse)Userviewrequest.this;
        String q="/userviewrequest?lid="+sh.getString("log_id","");
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
                problem=new String[ja1.length()];
                amount=new String[ja1.length()];
                date=new String[ja1.length()];
                statuss=new String[ja1.length()];
                rid=new String[ja1.length()];

                value=new String[ja1.length()];

                for(int i = 0;i<ja1.length();i++)
                {
                    rid[i]=ja1.getJSONObject(i).getString("request_id");
                    shopname[i]=ja1.getJSONObject(i).getString("shopname");
                    problem[i]=ja1.getJSONObject(i).getString("problem");
                    amount[i]=ja1.getJSONObject(i).getString("amount");
                    date[i]=ja1.getJSONObject(i).getString("date");
                    statuss[i]=ja1.getJSONObject(i).getString("status");
                    value[i]="Shopname: "+shopname[i]+"\nProblem: "+problem[i]+"\nAmount: "+amount[i]+"\nDate: "+date[i]+"\nStatuss: "+statuss[i];

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
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);

    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        rids=rid[position];
        stat=statuss[position];
        amounts=amount[position];
        if (stat.equalsIgnoreCase("accept"))
        {
            final CharSequence[] items = {"Payment","Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(Userviewrequest.this);
            // builder.setTitle("Add Photo!");
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                   if (items[item].equals("Payment")) {

                        startActivity(new Intent(getApplicationContext(),Usermakepayment.class));
                    }

                    else if (items[item].equals("Cancel")) {
                        dialog.dismiss();
                    }
                }

            });
            builder.show();
        }
    }
}