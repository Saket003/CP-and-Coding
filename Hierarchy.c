#include<stdio.h>
#include<stdlib.h>
#include <string.h>

//Assn 10
struct Node
{
    int data;
    struct Node* next;
};

// create a node with data as x
struct Node* create_node(int x) {
    struct Node* ptr = malloc(sizeof(struct Node));
    ptr->next = NULL;
    ptr->data = x;
    return ptr;
}

// delete the node at `ptr` and free its memory
void delete_node(struct Node* ptr) {
    free(ptr);
}

// ------------------------------ Node struct definition ends here ------------------------------

// Use this to operate on the list, this will always point at the head of the list.
struct Node* PythonListHead = NULL;


// prints the list in space seperated format
void print_list(struct Node* head) {
    struct Node* cur = head;
    while(cur) {
        printf("%d ", cur->data);
        cur = cur->next;
    }
    printf("\n");
}


// helper function that returns pointer to `Node` at `position`
// if there is no such position, it returns NULL
struct Node* get_node_at_pos(int position) {
    int pos = 0;
    struct Node* cur = PythonListHead;
    while(cur) {
        if(pos == position) return cur;
        pos++;
        cur = cur->next;
    }
    return NULL;
}


// Return the number of elements in the list
int len() {
    int length = 0;
    struct Node* cur = PythonListHead;
    while(cur) {
        length++;
        cur = cur->next;
    }
    return length;
}


// Add an item to the end of the list
void append(int x) {
    struct Node* cur = PythonListHead;
    if(cur == NULL) {
        // no list exists, we have to create one
        PythonListHead = create_node(x);
    }
    else {
        int pos = len() - 1;
        struct Node* last_node = get_node_at_pos(pos);
        last_node->next = create_node(x);
    }
}

// Remove all items from the list
void clear() {
    struct Node* cur = PythonListHead;
    PythonListHead = NULL;
    while(cur) {
        struct Node* next_node = cur->next;
        delete_node(cur);
        cur = next_node;
    }
}


// Return the number of times x appears in the list.
int count(int x) {
    struct Node* cur = PythonListHead;
    int n = 0;
    while(cur) {
        if(cur->data == x) n++;
        cur = cur->next;
    }
    return n;
}

// Return the data of the node at `position` 
// if no such position, return -1
int getitem(int position) {
    struct Node* node_at_pos = get_node_at_pos(position);
    if(node_at_pos) {
        return node_at_pos->data;
    }
    else return -1;
}


// erase the node at position
// if no such position, do nothing
void erase(int position) {
    struct Node* node_at_pos = get_node_at_pos(position);
    if(!node_at_pos) return;

    // 2 cases now
    // if node_at_pos is the first node
    if(node_at_pos == PythonListHead) {
        PythonListHead = PythonListHead->next;
        delete_node(node_at_pos);
    }
    else {
        struct Node* previous_node = get_node_at_pos(position-1);
        previous_node->next = node_at_pos->next;
        delete_node(node_at_pos);
    }
}

//Assn 10 end

// The following is a employee in the organisation, it has the pointer to two more employees a subordinate_1 and a subordinate_2
struct Employee {
    int emp_id; // emp_ids will be unique
    struct Employee* subordinate_1;
    struct Employee* subordinate_2;
};

// The following function creates a employee and returns its pointer
struct Employee* create_employee(int x) {
    struct Employee* ptr = (struct Employee*) malloc(sizeof(struct Employee));
    ptr->emp_id = x;
    ptr->subordinate_1 = NULL;
    ptr->subordinate_2 = NULL;
    return ptr;
}

// The following code creates a organisation from scanning the input file
struct Employee* create_company() {
    int x;
    scanf("%d", &x);

    if(x == -1) return NULL; // -1 is used when there is a NULL pointer ie when no value is present
    struct Employee* par = create_employee(x);

    par->subordinate_1 = create_company();
    par->subordinate_2 = create_company();
    
    return par;
}

// The following function 
void print_company_helper(struct Employee* ceo) {
    // take input
    if(!ceo) {
        printf("%d ", -1);
        return;
    }
    printf("%d ", ceo->emp_id);
    print_company_helper(ceo->subordinate_1);
    print_company_helper(ceo->subordinate_2);
    return;
}

void print_company(struct Employee* ceo) {
    print_company_helper(ceo);
    printf("\n");
    return;
} 

// --------------------------------------------------- YOU CAN EDIT BELOW THIS LINE -----------------------------------

struct Employee* CEO = NULL;
// CEO is a global pointer that points to the CEO of the company
struct Employee* Head = NULL;
/*  In this function you have to print all the employees at a given level, Note that ceo is at level 0
In any of the functions which involve printing you need not print -1 for NULL pointers */
int cnt=0;
int copy=0;
int diameter = 0;
int dia_count = 0;

void GetHead(struct Employee* cur, int emp_id){
    if(cur->emp_id == emp_id)
    {
    Head = cur;
    return;
    }
    if(cur->subordinate_1!=NULL){
        GetHead(cur->subordinate_1, emp_id);
    }
    if(cur->subordinate_2!=NULL){
        GetHead(cur->subordinate_2, emp_id);
    }
    return;
}

void Iterate(struct Employee* cur, int emp_id){
    if(cur->emp_id == emp_id){
    copy = cnt;
    return;
    }
    cnt++;
    if(cur->subordinate_1!=NULL){
        Iterate(cur->subordinate_1, emp_id);
    }
    if(cur->subordinate_2!=NULL){
        Iterate(cur->subordinate_2, emp_id);
    }
    cnt--;
    return;
}


// The following function returns the level of a employee with the given emp_id
int Level(int emp_id) {
    Iterate(CEO,emp_id);
    int num = copy;
    copy = 0;
    return (num);
}

void IterateLvl(struct Employee* cur, int level){
    if(Level(cur->emp_id)==level){
    printf("%d ",cur->emp_id);
    return;
    }
    if(cur->subordinate_1!=NULL){
        IterateLvl(cur->subordinate_1, level);
    }
    if(cur->subordinate_2!=NULL){
        IterateLvl(cur->subordinate_2, level);
    }
    return;
}

void EmployeesAtSameLevel(int level) {
    if(CEO==NULL)
        return;
    if(level==0){
        printf("%d",CEO->emp_id);
        return;
    }
    IterateLvl(CEO,level);
    return;
}

// You have to print the employees as you search the organization look for the examples in the pdf and the input.txt and output.txt for details
// Note: You do not have to print -1 for NULL pointers

void get_employees() {
    if(CEO == NULL)
    return;
    if(cnt==0)
    Head = CEO;
    struct Employee* copy = Head;
    printf("%d ",Head->emp_id);
    cnt++;
    if(Head->subordinate_1 !=NULL){
        Head = Head->subordinate_1;
        get_employees();
    }
    Head = copy;
    if(Head->subordinate_2 !=NULL){
        Head = Head->subordinate_2;
        get_employees();
    }
    Head = copy;
    cnt--;
    //if(cnt==0)
    //printf("\n");
    return;
}

/* In the following function you have to print the immediate team of a employee - it includes their boss and their subordinates
Note: You do not have to print -1 for NULL pointers */

void IterateBoss(struct Employee* cur,int emp_id){
    if(cur->subordinate_1!=NULL){
        if(cur->subordinate_1->emp_id == emp_id)
            copy = cur->emp_id;
        IterateBoss(cur->subordinate_1, emp_id);
    }
    if(cur->subordinate_2!=NULL){
        if(cur->subordinate_2->emp_id == emp_id)
            copy = cur->emp_id;
        IterateBoss(cur->subordinate_2, emp_id);
    }
    return;
}

/* The following function takes an emp_id this will belong to a employee in the organisation and your task is to return the emp_id of its boss
Note: If the boss does not exit return -1 */
int Boss(int emp_id) {
    if(CEO->emp_id == emp_id)
        return -1; 
    IterateBoss(CEO,emp_id);
    int n = copy;
    copy = 0;
    return n;
}

void ImmediateTeam(int emp_id) {
    if(CEO->emp_id == emp_id){
        if(CEO->subordinate_1!=NULL)
            printf("%d ",CEO->subordinate_1->emp_id);
        if(CEO->subordinate_2!=NULL)
            printf("%d ",CEO->subordinate_2->emp_id);
    }
    else{
        printf("%d ",Boss(emp_id));
        GetHead(CEO,emp_id);
        if(Head->subordinate_1!=NULL)
            printf("%d ",Head->subordinate_1->emp_id);
        if(Head->subordinate_2!=NULL)
            printf("%d ",Head->subordinate_2->emp_id);
    }
    Head = CEO;
    return;
}



// The following function gives the distance between employees with emp_id1 and emp_id2
int Distance(int emp_id1, int emp_id2) {
    if(emp_id1 == emp_id2)
    return 0;
    int i=-1,j=-1;
    int dist = 0, c=0;
    int vari,varj;
    vari=(emp_id1);//Boss
    while(vari!=-1)
    {
        i++;
        varj=(emp_id2);//Boss
        while(varj!=-1)
        {
            j++;
            if(vari==varj && c==0){
                dist = i+j;
                c++;
            }
            varj = Boss(varj);
        }
        j=-1;
        vari = Boss(vari);
    }
    return dist;
}

/* The following function returns the diameter of a Organisation - 
a diameter is the maximum distance between any two emp_ids in the organisation. You can use the distance function implemented above */

void LLMaker(){
    if(CEO == NULL)
    return;
    if(cnt==0)
    Head = CEO;
    struct Employee* copy = Head;
    if(cnt==0 || (Head->subordinate_1==NULL && Head->subordinate_2==NULL))
        append(Head->emp_id);
    cnt++;
    if(Head->subordinate_1 !=NULL){
        Head = Head->subordinate_1;
        LLMaker();
    }
    Head = copy;
    if(Head->subordinate_2 !=NULL){
        Head = Head->subordinate_2;
        LLMaker();
    }
    Head = copy;
    cnt--;
    return;
}

int TeamSize(int emp_id) {
    int n = 0;
    if(CEO->emp_id == emp_id){
        if(CEO->subordinate_1!=NULL)
        n++;
        if(CEO->subordinate_2!=NULL)
        n++;
    }
    else{
        GetHead(CEO,emp_id);
        n++;
        if(Head->subordinate_1!=NULL)
        n++;
        if(Head->subordinate_2!=NULL)
        n++;
    }
    Head = CEO;
    return n;
}


int Diameter() {
    if(dia_count!=0)
        return diameter;
    if(CEO==NULL)
        return 0;
    if(TeamSize(CEO->emp_id)==0)
        return 0;
    LLMaker();
    int max=-1;
    for(int i=0;i<len();i++)
    {
        for(int j=i+1;j<len();j++)
        {
            int t = Distance(getitem(i),getitem(j));
            if(t>max)
                max = t;
        }
    }
    clear();
    dia_count++;
    diameter = max;
    return max;
}

/* The following function takes an emp_id of a employee and returns the number of employees directly connected to it.
NULL pointers are not included */


// --------------------------------------------------- YOU CAN EDIT ABOVE THIS LINE -----------------------------------

/* The following driver code creates a organisation for you and based on the input file
it will call all the functions that are necessary, your job is to edit the functions
above the line. Their descriptions are in the pdf and in the comments in the code. */

int main(int argc, char const *argv[])
{
    CEO = create_company();
    print_company(CEO);

    int T; 
    scanf("%d", &T);

    char operation_type[50];

    while(T--) {
        scanf("%s", operation_type);

        if(strcmp(operation_type, "level") == 0) {
            int x;
            scanf("%d", &x);
            int d = Level(x);
            printf("%d\n", d);
        } 

        if(strcmp(operation_type, "distance") == 0) {
            int x, y;
            scanf("%d %d", &x, &y);
            int d = Distance(x, y);
            printf("%d\n", d);
        }

        if(strcmp(operation_type, "employees_at_same_level") == 0) {
            int x;
            scanf("%d", &x);
            EmployeesAtSameLevel(x);
            printf("\n");
        }

        if(strcmp(operation_type, "get_employees") == 0) {
            get_employees();
            printf("\n");
        }

        if(strcmp(operation_type, "boss") == 0) {
            int x;
            scanf("%d", &x);
            int d = Boss(x);
            printf("%d\n", d);
        }

        if(strcmp(operation_type, "diameter") == 0) {
            int d = Diameter();
            printf("%d\n", d);
        }

        if(strcmp(operation_type, "immediate_team") == 0) {
            int x;
            scanf("%d", &x);
            ImmediateTeam(x);
            printf("\n");
        }

        if(strcmp(operation_type, "team_size") == 0) {
            int x;
            scanf("%d", &x);
            int d = TeamSize(x);
            printf("%d\n", d);
        }
    }

    return 0;
}