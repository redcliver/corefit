#ifndef  _PROTOCOL_Optics
#define  _PROTOCOL_Optics

#ifdef _OT_CPP_
#undef _OT_CPP_
#endif

#define PS_MAXWAITTIME 2000
#define DELAY_TIME     150
///////////////////���󷵻���////////////////////
#define PS_OK                0x00
#define PS_COMM_ERR          0x01
#define PS_NO_FINGER         0x02
#define PS_GET_IMG_ERR       0x03
#define PS_FP_TOO_DRY        0x04
#define PS_FP_TOO_WET        0x05
#define PS_FP_DISORDER       0x06
#define PS_LITTLE_FEATURE    0x07
#define PS_NOT_MATCH         0x08
#define PS_NOT_SEARCHED      0x09
#define PS_MERGE_ERR         0x0a
#define PS_ADDRESS_OVER      0x0b
#define PS_READ_ERR          0x0c
#define PS_UP_TEMP_ERR       0x0d
#define PS_RECV_ERR          0x0e
#define PS_UP_IMG_ERR        0x0f
#define PS_DEL_TEMP_ERR      0x10
#define PS_CLEAR_TEMP_ERR    0x11
#define PS_SLEEP_ERR         0x12
#define PS_INVALID_PASSWORD  0x13
#define PS_RESET_ERR         0x14
#define PS_INVALID_IMAGE     0x15
#define PS_HANGOVER_UNREMOVE 0X17
 

///////////////������//////////////////////////////
#define CHAR_BUFFER_A          0x01
#define CHAR_BUFFER_B          0x02
#define MODEL_BUFFER           0x03

//////////////////���ں�////////////////////////
#define COM1                   0x01
#define COM2                   0x02
#define COM3                   0x03

//////////////////������////////////////////////
#define BAUD_RATE_9600         0x00
#define BAUD_RATE_19200        0x01
#define BAUD_RATE_38400        0x02
#define BAUD_RATE_57600        0x03   //default
#define BAUD_RATE_115200       0x04

#define MAX_PACKAGE_SIZE_		350   // ���ݰ���󳤶�
#define CHAR_LEN_AES1711		1024  // 512->1024 [2009.11.12] AES1711ʹ��1024��Сģ��
#define CHAR_LEN_NORMAL			512	  // 512 ͨ�ð汾ʹ��512��С��ģ��

#ifdef _OT_CPP_
extern "C"
{
#endif

	//==============================================================================//
	int WINAPI	PSGetUSBDevNum(int* iNums);//��ȡ FG_USB �豸��
	int WINAPI	PSGetUDiskNum(int* iNums); //��ȡ UDISK �豸��
	int WINAPI	PSOpenDeviceEx(HANDLE* pHandle, int nDeviceType,int iCom=1,int iBaud=1,int nPackageSize=2,int iDevNum=0);
	int WINAPI	PSCloseDeviceEx(HANDLE hHandle);
//	int WINAPI	PSGetPacketSize(HANDLE);
	int WINAPI  JPSetPackSize(HANDLE hHandle=NULL, int nPackSize=2);
	int WINAPI	PSAutoOpen(HANDLE* pHandle,int *type, int nAddr=0xFFFFFFFF,UINT uPwd=0x00,int bVfy=1);
	//==============================================================================//
	///////////////////////////////////////////////
	//////             ָ��                  //////
	///////////////////////////////////////////////
	//�����ָ��¼ȡͼ��
	int WINAPI	PSGetImage(HANDLE hHandle,int nAddr);
	int WINAPI	PSGetImage_Enroll(HANDLE hHandle,int nAddr);	// 0x29 ע��ʱ��ȡͼ��	//2010.6.25 blue
	
	//����ԭʼͼ������ָ������
	int WINAPI	PSGenChar(HANDLE hHandle,int nAddr,int iBufferID);
	
	//��ȷ�ȶ�CharBufferA��CharBufferB�е������ļ�
	int WINAPI	PSMatch(HANDLE hHandle,int nAddr,int* iScore);
	
	//��CharBufferA��CharBufferB�е������ļ����������򲿷�ָ�ƿ�
//	int WINAPI	PSSearch(HANDLE hHandle,int nAddr,int iBufferID, int iStartPage, int iPageNum, int *iMbAddress);
	int WINAPI	PSSearch(HANDLE hHandle,int nAddr,int iBufferID, int iStartPage, int iPageNum, int *iMbAddress,int *iscore=NULL);
	
	//��CharBufferA��CharBufferB�е������ļ��ϲ�����ģ�����ModelBuffer
	int	WINAPI	PSRegModule(HANDLE hHandle,int nAddr);
	
	//��ModelBuffer�е��ļ����浽flashָ�ƿ���
	int WINAPI	PSStoreChar(HANDLE hHandle,int nAddr,int iBufferID, int iPageID);
	
	//��flashָ�ƿ��ж�ȡһ��ģ�嵽ModelBuffer
	int WINAPI	PSLoadChar(HANDLE hHandle,int nAddr,int iBufferID,int iPageID);
	
	//�������������е��ļ��ϴ�����λ��
	int WINAPI	PSUpChar(HANDLE hHandle,int nAddr,int iBufferID, unsigned char* pTemplet, int* iTempletLength);
	
	//����λ������һ�������ļ�������������
	int WINAPI	PSDownChar(HANDLE hHandle,int nAddr,int iBufferID, unsigned char* pTemplet, int iTempletLength);
	int WINAPI  PSDownChar_Test(HANDLE hHandle,int nAddr,int iBufferID, unsigned char* pTemplet, int iTempletLength,int nAddr1,int ipack=MAX_PACKAGE_SIZE_,WORD whead=0xEF01,WORD wCheck=0x0000,int iErr=0);

	//�ϴ�ԭʼͼ��
	int WINAPI	PSUpImage(HANDLE hHandle,int nAddr,unsigned char* pImageData, int* iImageLength);
	
	//����ԭʼͼ��
	int WINAPI	PSDownImage(HANDLE hHandle,int nAddr,unsigned char *pImageData, int iLength);
	
	//�ϴ�ԭʼͼ��
	int WINAPI	PSImgData2BMP(unsigned char* pImgData,const char* pImageFile);
	
	//����ԭʼͼ��
	int WINAPI	PSGetImgDataFromBMP(HANDLE hHandle,const char *pImageFile,unsigned char *pImageData,int *pnImageLen);
	
	//ɾ��flashָ�ƿ��е�һ�������ļ�
	int WINAPI	PSDelChar(HANDLE hHandle,int nAddr,int iStartPageID,int nDelPageNum);
	
	//���flashָ�ƿ�
	int WINAPI	PSEmpty(HANDLE hHandle,int nAddr);
	
	//��������
	int WINAPI	PSReadParTable(HANDLE hHandle,int nAddr,unsigned char* pParTable);

	//++��Flash
	int WINAPI	PSReadInfPage(HANDLE hHandle,int nAddr, unsigned char* pInf);

	//++��������
//	int WINAPI	PSHighSpeedSearch(HANDLE hHandle,int nAddr,int iBufferID, int iStartPage, int iPageNum, int *iMbAddress);
	int WINAPI	PSHighSpeedSearch(HANDLE hHandle,int nAddr,int iBufferID, int iStartPage, int iPageNum, int *iMbAddress,int *iscore=NULL);

	//++����Чģ�����
	int WINAPI	PSTemplateNum(HANDLE hHandle,int nAddr,int *iMbNum);

	//++ָ��ͼϸ��
	int WINAPI	PSGenBinImage(HANDLE hHandle,int nAddr, int nImgType);
	
	//����ָ��
	int WINAPI	PSPowerDown(HANDLE hHandle,int nAddr);
	
	//�����豸���ֿ���
	int WINAPI	PSSetPwd(HANDLE hHandle,int nAddr,unsigned char* pPassword);
	
	//��֤�豸���ֿ���
	int WINAPI	PSVfyPwd(HANDLE hHandle,int nAddr,unsigned char* pPassword);
	
	//ϵͳ��λ�������ϵ��ʼ״̬
	int WINAPI	PSReset(HANDLE hHandle,int nAddr);
		
	//�����±�
	int WINAPI	PSReadInfo(HANDLE hHandle,int nAddr,int nPage,unsigned char* UserContent);
	
	//д���±�
	int WINAPI	PSWriteInfo(HANDLE hHandle,int nAddr,int nPage,unsigned char* UserContent);

	//++ע��ģ��
	int WINAPI	PSEnroll(HANDLE hHandle,int nAddr,int* nID);
	
	//++дģ��Ĵ���
	int WINAPI	PSWriteReg(HANDLE hHandle,int nAddr,int iRegAddr,int iRegValue);
	//дģ��Ĵ���������������
	int WINAPI	PSSetBaud(HANDLE hHandle,int nAddr,int nBaudNum);
	//дģ��Ĵ�������ȫ�ȼ�����
	int WINAPI	PSSetSecurLevel(HANDLE hHandle,int nAddr,int nLevel);
	//дģ��Ĵ��������ݰ���С����
	int WINAPI	PSSetPacketSize(HANDLE hHandle,int nAddr,int nSize);
	
	int WINAPI	PSUpChar2File(HANDLE hHandle,int nAddr,int iBufferID, const char* pFileName);
	int WINAPI	PSDownCharFromFile(HANDLE hHandle,int nAddr,int iBufferID, const char* pFileName);
	
	//��ȡ�����
	int WINAPI	PSGetRandomData(HANDLE hHandle,int nAddr,unsigned char* pRandom);

	//����оƬ��ַ
	int WINAPI	PSSetChipAddr(HANDLE hHandle,int nAddr,unsigned char* pChipAddr);

	//++�Զ���ָ֤��
	int WINAPI	PSIdentify(HANDLE hHandle,int nAddr,int *iMbAddress);
	
	int WINAPI	PSDoUserDefine(HANDLE hHandle,int nAddr,int GPIO,int STATE);

	///////////////////////////////////////////////////////////////////////++2008-12-12
	int WINAPI	PSUpdatOnline(HANDLE hHandle,int nAddr,unsigned char *pImageData, int iLength);
	int WINAPI	PSBurnCode(HANDLE hHandle,int nAddr,int nType,unsigned char *pImageData, int iLength);
	int WINAPI	PSPortControl(HANDLE hHandle,int nAddr,BOOL bOpen);
	int WINAPI	PSFingerData2BMPData(unsigned char *pFingerData, unsigned char *pBMPData,int* nBMPDataLen);
	int WINAPI	PSShowFingerData(HWND hWnd,unsigned char *pFingerData);
	///////////////////////////////////////////////////////////////////////++

	//��ģ��������	nPage,0,1,2,3��Ӧģ���0-256��256-512��512-768��768-1024
	int WINAPI	PSReadIndexTable(HANDLE hHandle,int nAddr,int nPage,unsigned char* UserContent);

	//�Զ��巢�Ͱ�	2009-03-04
	//pRecvData=NUllʱ����ʾ���ֽ��ȡ����
	int	WINAPI	PS_SB(HANDLE hHandle,int nAddr,unsigned char *pSendData,int iLen,unsigned char *pRecvData,int *pRecvLen,int flag=1);
	
	#define DEVICE_USB		0
	#define DEVICE_COM		1
	#define DEVICE_UDisk	2
		
	#define IMAGE_X 256
	#define IMAGE_Y 288
	
	//���ݴ���Ż�ȡ������Ϣ
	char* WINAPI	PSErr2Str(int nErrCode);

	///////////////////////////////////////////////////////////////////////2010-03-26
	int	WINAPI	PSEnableTestMsg(int bEl_S, int bEl_R);
	void TestMsg(unsigned char *pData,int iLen,char* msg=NULL,int bRS=0);//bRS=0[SendData] 1[RecvData]
	///////////////////////////////////////////////////////////////////////

	//����ELF�����Ķ����ݵ�Ŀ��� 0x28 2010-09-03
	int WINAPI	PSDownElfData(HANDLE hHandle, int nAddr, int nAddr_Data, unsigned char* pElfData, int nLen, int nIdx=1, CProgressCtrl *pro=NULL);
	int WINAPI	PSTestPro(CProgressCtrl* pro=NULL,int tm=100);

	//0x37	��������ELFDat���ݣ������ݣ� ���� 2011-08-26
	int WINAPI	PSDownElfDataX(HANDLE hHandle, int nAddr, int nAddr_Data, unsigned char* pElfData, int nLen, int nIdx=1, CProgressCtrl *pro=NULL);

	//////////////////////////////////////////////////////////////////////////
	//��������
	int WINAPI  PSSetCharLen(int nLen = CHAR_LEN_NORMAL);//��������ģ���Ĵ�С ͨ��-512 AES1711-1024
	int WINAPI	PSGetCharLen(int *pnLen);//��ȡ1ö�����Ĵ�С

#ifdef _OT_CPP_
}
#endif

#endif                                                     