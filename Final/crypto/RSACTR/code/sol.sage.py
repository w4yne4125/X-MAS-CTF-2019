from Crypto.Util.number import *

n = 94428988733647701630056905251472031968611314927435482986637131325766848502340510411170348022758798479988956098744202100362730955952872334219960340914746610088945223586010323647133931985137330988090265447798062946714175478248000203597185428732686578686165628015074682069068379879456380213303223762482421464803
e = 3
cipher = "008aff8713ae3cc9bffbada3d33547bed20d8b8dc0ce4bded98c8c037190ba9c7a2a13cf1792c45af44832cf89fe6fa70863c2da59687751ff69a0e7c6c80e2bda4f6c00fa1bd1cc6c848c7179d40242e7c803100ed63589d5ab0e870fa52c9ec03de39e88bb3542c8e0eb2fe27ca17f1c2a206a0119bf7f99d2ecca993c7cad"
val = "6d13c28b28375fa377cf85387132ffc9952db9bac107e61226a35f91f29ce10f53f3203e3f1b2f9104b249814d77d3a32103e2e2957420bc7506eb7e7b3900ccfdb995848a86e6e9676e514f2fc13e597539266372ae6b3930e750a467c903ff2c9cd5bdb707b91b17579add2a1f91030762993abcb3b4393087d41cf18ed8cc31bc12bc1e8271a126595f63e30d900f25999c70d968491d2ebbd4ff3cb28d470f47afaa4996d081bb963a0fb0c3621bf3b15744ac9601278e1a3643f85150d38798cb7fa7a49dd893066dbf07b57365f79b98404e8e00d41d3cc6c753d9371ddb552bd528e3fc74c658ac011a8d7009830cb438332755ff0c77b17c75a9f7990c5e3b0af202e881b300ebc3439312d4bff7bb6f55b76f50221f55a8799cec5208a31bdd6a51f3d34eaf9ac0f9bd99a9a7e4fe23c4e382ce4cf4d768f0faaadf9a7e9fbe0f5f99a044b93b990456afcacd71d5c059e200c8b78d5aa88aaa44ac9638bc65af1bbf88e8ae03671157d954b7cc41c1b21d22fbcc2b374012f6c07c"
cipher = (int.from_bytes(bytes.fromhex(cipher), 'big') - bytes_to_long(bytes.fromhex('a' * 16))) % n

# cipher = 381280561446525777203821547743409979242405161796612594559654255340032514359155800744878244753916727872159230782777739794470546281051864475569442334518882850518079160570529292437322881273177132160309114324366307687699518868401382258439032471846355814342973081867492280134427111570131249722047745358715539971

flag = [val[:256], val[256:512], val[512:]]
flag = [int.from_bytes(bytes.fromhex(f), 'big')for f in flag]
nonce = pow(cipher, 3, n)

# flag = [76596605737693251406381267124630555446638314818747631679581424995948957389604239798184125881522385470288256245284818286829723878150343138461357097241669374581993625369861932438909063372252112939427562726656075708946411912492569699347882344748707251756085828090648821837498045238187467300331940638583990180044,
#  34924866567369537294364008382392848736515767972440091506565705137655602735604482159355705588340130105091585653239495864496157254259720044433578995363491098333879947274568183868109864860184784199474756756917132121376727322126345970873391589175236746568268794247303608546625818462987254864020276192133916522393,
#  8685167049105371794911184656836252528611506790042842453608223766341947644552099359985739630220989477176592772443079776147903495549966177033541665360630411477509961525690317294600801741911044864988372466494967021613870550475165229145551696718555466197523537493206914456598771474874351978998065637531497971836]

# nonce = 15164993831685148116784120697073395329718794566293795236397831333733976208444202129425286499295432026617887538914665190741324178505985208486272260945750658316499749700351094377542872435039525683833971631073387729138682109694608386186821285223014259193735973230884517437645531330769519920443457609894350504722

from Crypto.Util.number import *
P.<x> = PolynomialRing(Zmod(n))

for i in range(3):
    f = -((flag[i] - x) ^ 3 - (nonce + 2020 * (i + 1)))

    roots = f.small_roots()
    if roots:
        root = roots[0]
        t = long_to_bytes(root)
        print(t)