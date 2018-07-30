using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Threading;

namespace fgdemo
{
    public partial class Form1 : Form
    {
       static VoicePlayer voicePlayer = new VoicePlayer();
        public Form1()
        {
            InitializeComponent();
        }
        static IntPtr phandler = IntPtr.Zero;
        static UInt32 nAddr = 0xffffffff;

        //ThreadStart startEnroll = new ThreadStart(Enroll);

        //Thread EnrollThread = new Thread(startEnroll); 
        static Thread EnrollThread = new Thread(new ThreadStart(Enroll));


        //Open Devies
        private void button1_Click(object sender, EventArgs e)
        {
            //IntPtr[] phandler=new IntPtr[1];
            var ret=-1;
            //IntPtr phandler = IntPtr.Zero;

            //UInt32 nAddr = 0xffffffff;
            //int nAddr = 4294967295;

            //UInt32 pwd = 0x6F616978;
            UInt32 pwd = 0;
            
            ret = fgapi.PSOpenDeviceEx(ref phandler, 2, 1, 1, 2, 0);
            if (ret == 0)
            {
                //IntPtr handler = IntPtr.Zero;
                ret = fgapi.PSVfyPwd(phandler, nAddr, ref pwd);
                if (ret == 0)
                {
                    this.textBox1.Clear();
                    this.textBox1.Text = "Open ok!";
                    //voicePlayer.VoicePlay("001");
                }
                else
                {
                    this.textBox1.Text = "Open fail!";
                    //voicePlayer.VoicePlay("002");
                }
            }
        }

        //Get image
        private void button2_Click(object sender, EventArgs e)
        {
            //UInt32 nAddr = 0xffffffff;
            int ret = -1;
            int i=0;
            byte[] ImageData = new byte[256*288];
            int ImageLength = 0;
            string ImagePath = "D:\\Finger.bmp";
            ret = fgapi.PSGetImage(phandler, nAddr);
            if (ret == 0)
            {
                this.textBox1.Clear();
                this.textBox1.Text = "Get image ok!";
                ret = fgapi.PSUpImage(phandler, nAddr,ImageData, ref ImageLength);
                if (ret == 0)
                {
                    //this.textBox1.Clear();
                    this.textBox1.Text = "upload image ok!";
                    //voicePlayer.VoicePlay("003");
                    ret = fgapi.PSImgData2BMP(ImageData, ImagePath);
                    if (ret == 0)
                    {
                        this.textBox1.Text = "Save image D:\\Finger.bmp";
                        //pictureBox1.Image = Image.FromFile("D:\\Finger.bmp");
                    }
                }
               
            }
            else
            {
                this.textBox1.Text = "get image fail!";
                //voicePlayer.VoicePlay("004");
            }
        }

        //Register
        private void button3_Click(object sender, EventArgs e)
        {
            int  ret=-1;
            //voicePlayer.VoicePlay("005");
            ret = fgapi.PSGetImage(phandler, nAddr);
            if(ret == 0){
                ret=fgapi.PSGenChar(phandler, nAddr,1);
                if (ret == 0)
                {
                    ret = fgapi.PSGetImage(phandler, nAddr);
                    if (ret == 0)
                    {
                        ret = fgapi.PSGenChar(phandler, nAddr, 2);
                        if (ret == 0)
                        {
                            ret = fgapi.PSRegModule(phandler, nAddr);
                            if (ret == 0)
                            {
                                ret = fgapi.PSStoreChar(phandler, nAddr, 1, 1);
                                if (ret == 0)
                                {
                                    this.textBox1.Text = "register fingerprint ok!";
                                    //voicePlayer.VoicePlay("006");
                                }
                            }
                        }
                    }
                    
                }
            }
        }

        //Search fingerprint
        private void button4_Click(object sender, EventArgs e)
        {
            int ret=-1;
            int iMbAddress=0;
            int iscore=0;
            int fgnum = 0;
             ret = fgapi.PSGetImage(phandler, nAddr);
            if(ret == 0)
            {
                ret=fgapi.PSGenChar(phandler, nAddr,1);
                if (ret == 0)
                {
                    
                    fgapi.PSTemplateNum(phandler, nAddr, ref fgnum);
                    fgapi.PSSearch(phandler, nAddr, 0x01, 0, fgnum+1, ref iMbAddress, ref iscore);
                    if (iscore > 50)
                    {
                        //voicePlayer.VoicePlay("007");
                        this.textBox1.Text = "Search ok at " + Convert.ToString(iscore);
                    }
                    else
                    {
                         //voicePlayer.VoicePlay("008");
                         this.textBox1.Text = "Search Fail";
                    }
                }
            }
        }

        //Delete one fingerprint
        private void button5_Click(object sender, EventArgs e)
        {
            int ret = -1;
            int delstartid = 0;
            int fgnum = 0;
            fgapi.PSTemplateNum(phandler, nAddr,ref fgnum);

            ret = fgapi.PSDelChar(phandler, nAddr, delstartid, 1);
            if (ret == 0)
            {
                //voicePlayer.VoicePlay("009");
                this.textBox1.Text = "Totol" + Convert.ToString(fgnum) + "fingerprint,delete index " + Convert.ToString(delstartid) + " success";
            }
        }

        //upload fingerprint
        private void button6_Click(object sender, EventArgs e)
        {
            int ret = -1;
            byte[] pbuf = new byte[1024+1];
            int len = 0;
            int saveFgnum = 1;
            string path = @"d:\FGTemplet.mb";
            FileStream fs = new FileStream(path, FileMode.CreateNew);
            ret = fgapi.PSLoadChar(phandler, nAddr, 0x01, saveFgnum);       //this upload one fingerprint,you can upload more
            if (ret == 0)
            {
                ret = fgapi.PSUpChar(phandler, nAddr, 0x01, pbuf, ref len);
                if (ret == 0)
                {
                    fs.Write(pbuf, 0, pbuf.Length);
                    fs.Close();
                    this.textBox1.Text = "upload ok";
                    //voicePlayer.VoicePlay("010");
                }
            }
        }

        //load fingerprint
        private void button7_Click(object sender, EventArgs e)
        {
            int ret = -1;
            int fgid = 1;  // load address
            byte[] pbuf = new byte[1024 + 1];  
            int len = 0;

            string path = @"d:\FGTemplet.mb";
            FileStream fs = new FileStream(path, FileMode.Open, FileAccess.Read);
            BinaryReader r = new BinaryReader(fs);
            fs.Seek(0, SeekOrigin.Begin);
            fs.Read(pbuf, 0, 1024);
            fs.Close();
            len = 1024;
            ret=fgapi.PSDownChar(phandler, nAddr, 0x01, pbuf, len);
            if (ret == 0)
            {
                ret = fgapi.PSStoreChar(phandler, nAddr, 1, fgid);
                if(ret == 0)
                {
                    //voicePlayer.VoicePlay("011");
                    this.textBox1.Text = "load ok";
                }
            }



        }

        //clear
        private void button8_Click(object sender, EventArgs e)
        {
            int ret = -1;
            ret = fgapi.PSEmpty(phandler, nAddr);
            if (ret == 0)
            {
                this.textBox1.Text = "clear ok";
                //voicePlayer.VoicePlay("011");
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {


            EnrollThread.Start();//start thread

        }


        private static void Enroll()
        {
            int ret = -1;
            int times = 0;
            while (true)
            {
                voicePlayer.VoicePlay("005");
                ret = fgapi.PSGetImage(phandler, nAddr);
                if (ret == 0)
                {
                    ret = fgapi.PSGenChar(phandler, nAddr, 1);
                    if (ret == 0)
                    {
                        ret = fgapi.PSGetImage(phandler, nAddr);
                        if (ret == 0)
                        {
                            ret = fgapi.PSGenChar(phandler, nAddr, 2);
                            if (ret == 0)
                            {
                                ret = fgapi.PSRegModule(phandler, nAddr);
                                if (ret == 0)
                                {
                                    ret = fgapi.PSStoreChar(phandler, nAddr, 1, 1);
                                    if (ret == 0)
                                    {
                                        //this.textBox1.Text = "enroll ok! ";
                                        //voicePlayer.VoicePlay("006");
                                        EnrollThread.Abort();
                                    }
                                }
                            }
                        }

                    }
                }
                if (ret != 0)
                {
                    times++;
                    Thread.Sleep(1000); 
                    continue;
                }
                if (times > 10)
                {
                    EnrollThread.Abort();
                }
            }
        }



    }
}





