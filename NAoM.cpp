#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Rule {
    string symbol;
    string arrow;
    string replacement;
};

class MarkovAlgorithm {
public:
    MarkovAlgorithm(string alph) {
        alphabet = alph;
    }
    void addRule(const string& symbol, const string& arrow, const string& replacement) 
    {
        if (this->checkString(this->alphabet, symbol) && this->checkString(this->alphabet, replacement)) {
            Rule rule;
            rule.symbol = symbol;
            rule.arrow = arrow;
            rule.replacement = replacement;
            rules.push_back(rule); // Добавление правила преобразования
        }
        else {
            cout << "Неверная подстрока в правиле! Подстрока должна состоять из символов алфавита!" << endl;
        }
    }

    string applyRules(const string& input) 
    {
        if (this->checkString(this->alphabet, input)) {
            string output = input;
            bool haltAfterStar = false;
            for (size_t i = 0; i < rules.size(); ++i)
            {
                if (haltAfterStar) break;
                size_t pos = 0;
                while ((pos = output.find(rules[i].symbol, pos)) != std::string::npos)
                {
                    output.replace(pos, rules[i].symbol.length(), rules[i].replacement);
                    if (rules[i].arrow == "->*")
                    {
                        haltAfterStar = true;
                        break;
                    }
                    pos += rules[i].replacement.length();
                }
            }
            return output;
        }
        else {
            cout << "Неправильная входная строка!" << endl;
            return "";
        }
    }
    private:
        vector<Rule> rules; // Правила преобразования
        string alphabet; // Алфавит
        bool checkString(const string& alphabet, const string& InputString) {
            for (int i = 0; i <= InputString.size() - 1; i++) {
                int is_in_alph = alphabet.find(InputString[i]);
                if (is_in_alph == -1) {
                    return false;
                }
            }
            return true;
        }
};

int main() {
    setlocale(LC_ALL, "");
    
    string alphabet, initialString, symbol, arrow, replacement;
    
    cout << "Введите алфавит: ";
    getline(cin, alphabet);

    MarkovAlgorithm algorithm(alphabet);
    
    cout << "Введите начальную строку: ";
    getline(cin, initialString);

    
    
    cout << "Введите преобразования (символ, стрелку и замену через пробел, для завершения введите 'x'):\n";
    while (cin >> symbol && symbol != "x" && cin >> arrow && arrow != "x" && cin.get() && getline(cin, replacement) && !replacement.empty()) 
    {
        algorithm.addRule(symbol, arrow, replacement);
    }
    
    string result = algorithm.applyRules(initialString);
    cout << "Результат после применения алгоритма Маркова: " << result << endl;
    
    return 0;
}
