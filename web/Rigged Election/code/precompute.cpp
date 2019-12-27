#include <string>
#include <iostream>
#include <openssl/md5.h>
#include <map>
using namespace std;

string MD5(const string& src ){
    MD5_CTX ctx;

    string md5_string;
    unsigned char md[16] = { 0 };
    char tmp[33] = { 0 };

    MD5_Init( &ctx );
    MD5_Update( &ctx, src.c_str(), src.size() );
    MD5_Final( md, &ctx );

    for( int i = 0; i < 16; ++i )
    {   
        memset( tmp, 0x00, sizeof( tmp ) );
        sprintf( tmp, "%02X", md[i] );
        md5_string += tmp;
    }   
    return md5_string;
}
map<string, long long> mp;
int main(int argc, char **argv){
    char buf[100];
    string prefix = "watch__bisqwit__";
    for(long long i = 0;i < 20000000; i ++){
        sprintf(buf, "%s%lld", prefix.c_str(), i);
        string ret = MD5(buf).substr(0, 6);
        printf("%s %lld\n", ret.c_str(), i);
    }
}