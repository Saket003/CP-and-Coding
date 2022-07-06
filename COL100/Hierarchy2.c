#include<stdio.h>
#include<stdlib.h>
#include <string.h>

//Assn 10 Start

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

// Return the data of the node at `position` 
// if no such position, return -1
int getitem(int position) {
    struct Node* node_at_pos = get_node_at_pos(position);
    if(node_at_pos) {
        return node_at_pos->data;
    }
    else return -1;
}

struct Node* reverse_helper(struct Node* cur_node) {
    if(cur_node == NULL) return NULL;

    if(cur_node->next == NULL) {
        // this is the first node of the reversed list
        PythonListHead = cur_node;
        return cur_node;
    }

    // recursively solve for the next node
    struct Node* next_node = reverse_helper(cur_node->next);

    // set the next of next_node to cur_node
    next_node->next = cur_node;

    // also make the cur_node->next as NULL, since cur_node is the last node of the list
    cur_node->next = NULL;

    return cur_node;
}

// Reverse the elements of the list in place.
// Make sure you change `PythonListHead` accordingly
void reverse() {
    struct Node* last_node = reverse_helper(PythonListHead);
}

// swaps the nodes present at `position` and `position+1`
// if either of  `position` or `position+1` does not exist, do nothing
void swap(int position) {
    struct Node* node_at_pos = get_node_at_pos(position);
    struct Node* next_node = get_node_at_pos(position+1);
    if(!node_at_pos || !next_node) return;

    // 2 cases 
    if(node_at_pos == PythonListHead) {
        PythonListHead = next_node;
        node_at_pos->next = next_node->next;
        next_node->next = node_at_pos;
    }
    else {
        struct Node* prev_node = get_node_at_pos(position-1);
        prev_node->next = next_node;
        node_at_pos->next = next_node->next;
        next_node->next = node_at_pos;
    }
}


// sort the Python list
// you may use the above defined swap function to 
// implement bubble sort. But its upto you, use whatever algorithm
// that you seem comfortable.
void sort() {
    int n = len();
    for(int i=0;i<n;i++) {
        for(int j=0;j<n-i-1;j++) {
            int x = get_node_at_pos(j)->data;
            int y = get_node_at_pos(j+1)->data;
            if(x > y) swap(j);
        }
    }
}

//Assn 10 end

// The following is a employee in the organisation, it has the pointer to two more employees a subordinate_1 and a subordinate_2
struct Employee {
    int emp_id; // emp_ids will be unique
    char* emp_name;
    int emp_salary;
    struct Employee* subordinate_1;
    struct Employee* subordinate_2;
};

// The following function creates a employee and returns its pointer
struct Employee* create_employee(int id, char* name, int salary) {
    struct Employee* ptr = (struct Employee*) malloc(sizeof(struct Employee));
    ptr->emp_id = id;
    ptr->emp_salary = salary;
    ptr->emp_name = strdup(name);
    // strdup() creates a copy of the string or char pointer and stores it in the new char pointer of the employee
    ptr->subordinate_1 = NULL;
    ptr->subordinate_2 = NULL;
    return ptr;
}

// The following code creates a organisation from scanning the input file
struct Employee* create_company() {
    int id, salary;
    char name[100];
    scanf("%d", &id);
    if(id == -1) return NULL; // -1 is used when there is a NULL pointer ie when no value is present

    scanf("%s %d", name, &salary);
    struct Employee* par = create_employee(id, name, salary);

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
    printf("%d %s %d ", ceo->emp_id, ceo->emp_name, ceo->emp_salary);
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
int copy;
double sum = 0.0;
int count = 0;
struct Employee* Head = NULL;
int level = -1;
int level_copy = -1;

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

// The below function returns the employee id of the first common boss
int get_first_common_boss(int emp_id1,int emp_id2){
    if(emp_id1 == emp_id2){
        if(CEO->emp_id ==emp_id1)
            return -1;
        return Boss(emp_id1);
    }
    int i=-1,j=-1;
    int boss_emp, c=0;
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
                boss_emp = vari;
                c++;
            }
            varj = Boss(varj);
        }
        j=-1;
        vari = Boss(vari);
    }
    return boss_emp;
}

// Print the bosses of the given employee in the order from CEO to immediate boss
void get_all_bosses(int emp_id){
    if(emp_id == CEO->emp_id){
        printf("-1");
        return;
    }
    while(Boss(emp_id)!=-1){
        append(Boss(emp_id));
        emp_id = Boss(emp_id);
    }
    reverse();
    for(int i=0;i<len();i++){
        printf("%d ",getitem(i));
    }
    clear();
    return;
}

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

//-----------------------------------------------------------------
//Print the employees with the same last name sperated by a space in the order of their level

void name_helper(struct Employee* cur, char last_name[]){
    if(!strcmp(last_name, cur->emp_name))
        append(cur->emp_id);
    if(cur->subordinate_1!=NULL){
        name_helper(cur->subordinate_1, last_name);
    }
    if(cur->subordinate_2!=NULL){
        name_helper(cur->subordinate_2, last_name);
    }
    return;
}

void GetLevel(struct Employee* cur, int emp_id){
    level++;
    if(cur->emp_id == emp_id){
        level_copy = level;
    }
    if(cur->subordinate_1!=NULL){
        GetLevel(cur->subordinate_1, emp_id);
    }
    if(cur->subordinate_2!=NULL){
        GetLevel(cur->subordinate_2, emp_id);
    }
    level--;
    return;
}

void same_last_names(int emp_id){
    GetHead(CEO,emp_id);
    char *last_name;  //Check max length of last name?
    last_name = Head->emp_name;
    name_helper(CEO,last_name);
    int x = 0, i=0;
    while(1){
        for(int j=0;j<len();j++){
            GetLevel(CEO,getitem(j));
            if(level_copy == i){
                printf("%d ",getitem(j));
                x++;
            }
            level_copy = -1;
        }
        if(x>=len())
            break;
        i++;
    }
    clear();
}

void Sum(struct Employee* cur){
    sum = sum + cur->emp_salary;
    count++;
    if(cur->subordinate_1!=NULL){
        Sum(cur->subordinate_1);
    }
    if(cur->subordinate_2!=NULL){
        Sum(cur->subordinate_2);
    }
    return;
}

// Return the average salary of the team with the given employee as head
double get_average_salary(int emp_id){
    GetHead(CEO,emp_id);
    Sum(Head);
    double avg_copy = (sum/count);
    sum = 0.0;
    Head = NULL;
    count = 0;
    return avg_copy;
}
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

    char operation_type[100];

    while(T--) {
        scanf("%s", operation_type);

        if(strcmp(operation_type, "get_first_common_boss") == 0) {
            int x,y;
            scanf("%d %d", &x, &y);
            int ans = get_first_common_boss(x,y);
            printf("%d\n", ans);
        } 
        else if(strcmp(operation_type, "same_last_names") == 0) {
            int x;
            scanf("%d", &x);
            same_last_names(x);
            printf("\n");
        } 
        else if(strcmp(operation_type, "get_all_bosses") == 0) {
            int x;
            scanf("%d", &x);
            get_all_bosses(x);
            printf("\n");
        } 
        else if(strcmp(operation_type, "get_average_salary") == 0) {
            int x;
            scanf("%d", &x);
            double ans = get_average_salary(x);
            printf("%.2f\n", ans);
        } 

    }

    return 0;
}
