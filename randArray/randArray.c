/**
 * @file randArray.c
 * @author  Vecang
 * @brief
 * @version 0.1
 * @date 2022-09-08
 *
 * @copyright Copyright (c) 2022
 *
 */
#include <stdio.h>
#include <stdlib.h>
//#include <time.h> //读取系统时间

void disorganise(int a[], int len);
void exchange(int *a, int *b);

int main(void)
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int len = (sizeof(a) / sizeof(a[0]));

    disorganise(a, len);

    for (int i = 0; i < len; i++)
    {
        printf("%d:\t%d\n", i, a[i]);
    }

    return 0;
}

void disorganise(int a[], int len)
{
    // srand((unsigned)time(NULL)); //读取系统时间（全随机）
    int rN1 = (rand() % len);// 随机index1
    int rN2 = (rand() % len);// 随机index2

    for (int i = 0; i < len; i++)
    {
        if (rN1 != rN2)//
        {
            exchange(&a[rN1], &a[rN2]);
        }
        rN1 = (rand() % len);
        rN2 = (rand() % len);
    }
}

void exchange(int *a, int *b)
{
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}