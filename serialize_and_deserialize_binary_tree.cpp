// 297. Serialize and Deserialize Binary Tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 /*
  * 重新做一遍，简化一下代码，理清思路。
  * 
  */
class Codec {
public:
    
    void serialize_helper(TreeNode* root, ostream& stream) {
        if (root == NULL) {
            stream << "$,";
            return;   
        }
        stream << root->val << ",";
        serialize_helper(root->left, stream);
        serialize_helper(root->right, stream);
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string data;
        ostringstream oss;
        serialize_helper(root, oss);
        cout << oss.str() <<endl;
        return oss.str();
    }
    
    bool readstream(istream& stream, int& number) {
        if (stream.eof())
            return false;
        char buffer[32];
        buffer[0] = '\0';
        char ch;
        stream >> ch;
        int i = 0;
        while(!stream.eof() && ch != ',') {
            buffer[i++] = ch;
            stream >> ch;
        }
        bool isNumeric = false;
        if (i > 0 && buffer[0] != '$') {
            buffer[i] = '\0'; // notice
            number = atoi(buffer);
            isNumeric = true;
        }
        
        return isNumeric; 
    }
    
    void deserialize_helper(TreeNode** root, istream& stream) {
        int number;
        if (readstream(stream, number)) {
            *root = new TreeNode(number);
            deserialize_helper(&((*root)->left),stream);
            deserialize_helper(&((*root)->right),stream);
        }
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
        TreeNode* root = NULL;
        deserialize_helper(&root, iss);
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));