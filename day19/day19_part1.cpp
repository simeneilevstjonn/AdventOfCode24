#include <string>
#include <iostream>
#include <cstring>
#include <vector>


const char* towels[] = {"bwb", "wrrbg", "ubwg", "rwg", "urbbgrr", "wugr", "rububww", "rbrw", "ggw", "grgwu", "wb", "gwuuubw", "gbr", "ugur", "rug", "ugw", "rg", "uru", "wgrbgug", "buwwrwu", "bbbuw", "urbug", "rrbr", "uwbr", "wurr", "wbwrw", "bug", "rggwguru", "brrgub", "uuwg", "gww", "gwb", "ubrb", "wgrg", "rubbgwu", "bbb", "buu", "gbgrwg", "rwuwbg", "uubwbu", "buuu", "uwurwgu", "gwbugwgw", 
"guru", "brww", "bwgrugb", "rbbgrw", "ruubg", "wub", "wbw", "bgww", "bgugg", "rru", "urrwuw", "bwwgw", "brbww", "gwug", "bwwwbwb", "uubggg", "gbgb", "rbgub", "bwuwgg", "wrbb", "buwrw", 
"gbbwrrg", "gug", "wuww", "u", "ru", "gbbbu", "ugwrwgb", "rgb", "rwwuwuwb", "ruugwrb", "rgruw", "wwuwwbbw", "urrrbu", "bwg", "ub", "urg", "ruwg", "bwr", "wbwb", "brbwrwww", "rbwgrgub", 
"gbb", "grwwb", "bwggw", "urwr", "rrrug", "buw", "gbbgrguu", "rbgg", "brbwur", "ububwb", "bur", "wruru", "buurbu", "ggb", "ggr", "rggwrub", "uwbbbbgb", "rrrb", "uwr", "bwwrr", "brgw", "urrwug", "gub", "rwwb", "wgw", "ggur", "bbrb", "uwrbgbu", "buubu", "urb", "bg", "gguubbrg", "gg", "rwr", "uubb", "wwb", "uwgbub", "brbgrrb", "ubbbrwb", "ugr", "ggwwug", "wbgbu", "grw", 
"wrb", "brr", "rub", "gr", "guwb", "ggrgr", "rrb", "uuurb", "brw", "wrg", "guw", "uggr", "uuurgw", "wrrgu", "wwuu", "uruuu", "bwrr", "wwg", "bwguu", "rugww", "rbw", "wur", "buuuw", "rwb", "bbg", "gbu", "rurw", "brwbbb", "wbbgguw", "rrrr", "bwbbb", "bgu", "uurbb", "gwrbwb", "wgwrgbwg", "wgrw", "gugw", "urrbb", "rww", "ruu", "uwbrbb", "bbbrwb", "bugw", "wug", "wgg", "rwru", "r", "uwg", "wggr", "brbwgb", "uwbuwg", "ubr", "rbgwrrw", "grwbur", "grrrbb", "wgr", "rrbw", "uurw", "wbgg", "buwg", "wru", "ruwwu", "wbbbrg", "grgbgbr", "uuu", "wrr", "ubwr", "rubbgb", "gbrw", "gbug", "uwrur", "ugru", "uruggr", "ubu", "uwgg", "wrgb", "wbg", "ug", "guu", "bgw", "wbu", "wuru", "rur", "wwbwwr", "wbugg", "wrwgwwb", "rrgu", "uuugg", "bgbb", "gb", "uwugwgu", "bguw", "ugwgwugb", "brburg", "grrbw", "brb", "bguwb", "bwugu", "ubwgg", "rbr", "wwrb", "bwgrug", "rbww", "gwg", "rgrgu", "bwbgrgb", "wwbu", "bwugw", "uguu", "uubuggwb", "uwb", 
"gbg", "uubur", "urwbub", "uggrr", "wrurb", "bbr", "uggg", "gur", "wrwrw", "bbbrug", "bbuw", "b", "wbgw", "bubgubg", "ggg", "bru", "gbuwr", "ruw", "wgu", "ubb", "gru", "bb", "uwbug", "ugbrgu", "uruwrrbb", "rrug", "bgbu", "ggwgbrr", "rwuuuuu", "bgr", "rrwu", "ruub", "burw", "bbww", "uuuu", "gwwb", "wrur", "grb", "br", "bwwgg", "gburg", "ugubw", "gbwbwbb", "gwrgubrg", "bguwwr", "grgugbw", "rugw", "guww", "brrrr", "uguurb", "uwwbbw", "guwgu", "guguubr", "rwu", "bbbwb", "wggru", "bub", "rwrg", "gw", "bw", "wrgbrb", "ggbru", "gwbw", "wuwgu", "rwgurr", "gugr", "rbu", "wrbguww", "uuww", "rbuwu", "uwu", "rburgwu", "wgbbuu", "rggrur", "wbr", "buubb", "rgwb", "bgg", "rwurbg", "urgrg", "rbrrr", "rbur", "wr", "uwuruggr", "buug", "wubw", "uubbbu", "gwu", "ubgg", "rgu", "uwwr", "brgrgw", "uuw", "wwr", "wu", "grgwbbb", "rgrbr", "bbu", "wuwgr", "rrg", "urw", "urgbgr", "bwwb", "gurgu", "rr", "rgr", "rbg", "rgrr", "uwgug", "gwggbw", "rgg", "ubgr", "ggww", "gugggr", "rrbgrw", "rrr", "ubw", "uw", "gbw", "wrww", "uwwwrwbu", "bgwrugu", "guur", "grrruuw", "ubrgg", "ggrb", "grg", "bgrru", "rurrb", "ugg", "wwgr", "uwbrg", "wuw", "ubbu", "rbb", "www", "wwubgu", "ur", "bububg", "gwr", "grgguwg", "bubr", "wwu", "ggru", "ugu", "rgrru", "uburu", "wuu", "wbugrwu", "uur", "urwgrwg", "bwgwgwg", "ubgru", "burugw", "wgbwrr", "urr", "wgb", "g", "ruwggg", "wbb", "bbrrg", "wbuw", "uubwugw", "rwrr", "uubgr", "uww", "gu", "uubu", "rrw", "ugb", "buuwr", "uug", "rbwbubgb", "wgwburur", "rrurr", "uguw", "wbrw", "ggu", "ruwgwb", "rgw", "ubrbgu", "ururb", "rb", "ruuu", "ubg", "rbbbggwu", "wg", "wbrbbg", "gwwwuu", "bugg", "uu", "rbgwrwu", "gggbbu", "rbggu", "wbwwr", "uwbbu", "ggrwu", "brg", "buub", "bggguu", "bu", "gbrubgwr", "wrwwb", "bbw", "wubrbb", "bbwbbur", "bww", "uwwuuw"};
// const char* towels[] = {"r", "wr", "b", "g", "bwu", "rb", "gb", "br"};


bool prefix_match(const char* pattern, const char* towel) 
{
    int pl = strlen(pattern);
    int tl = strlen(towel);

    if (pl < tl) 
    {
        return false;
    }

    return !strncmp(pattern, towel, tl);
}

std::vector<bool> impossible_offsets = std::vector<bool>();

bool can_make(const char* pattern) 
{
    if (!*pattern) 
    {
        return true;
    }

    if (impossible_offsets[strlen(pattern)])
    {
        // std::cout << "size is " << strlen(pattern) << " returning due to impossible offset\n";
        return false;
    }

    for (const char* towel : towels) 
    {
        if (prefix_match(pattern, towel) && can_make(pattern + strlen(towel))) 
        {
            return true;
        }
    }

    impossible_offsets[strlen(pattern)] = true;    
    return false;
}

int main() 
{
    std::string l;
    std::getline(std::cin, l);
    std::getline(std::cin, l);

    int possible = 0;

    for (std::string s; std::cin >> s; )
    {
        // std::cout << "Now processing " << s << ": ";

        impossible_offsets.resize(s.size() + 1);
        std::fill(impossible_offsets.begin(), impossible_offsets.end(), false);

        bool res = can_make(s.c_str());
        // std::cout << res << std::endl;


        possible += res;
    }

    std::cout << possible << std::endl;
}