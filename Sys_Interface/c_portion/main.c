#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct Mat
{
    float *arr;
    int h;
    int w;
} *Mat;

void    prMat(Mat inst);
Mat     mul(Mat m1, Mat m2);
float   getE(Mat m,int idx,int jdx);
Mat     getR(Mat m,int R);
Mat     getC(Mat m,int C);
float   rxc(Mat r,Mat c);

Mat newM(float *arr,int row,int col)
{
    Mat result = malloc(2*sizeof(int)+sizeof(float*));
    result->arr=arr;
    result->h=row;
    result->w=col;
    return result;
}

void main(void)
{
    printf("______________________________\nBeginning of test\n\n");

    /*float *a = malloc(4*sizeof(float));
    a[0]=1;
    a[1]=2;
    a[2]=2;
    a[3]=3;*/

    float a[] = {1,2,4,2,3,5};
    Mat ma = newM(a,2,3);

    float ident[] = {0,0,0,0};
    Mat idenTT = newM(ident,2,2);

    float rv[] = {1,2,3};
    Mat rM = newM(rv,1,3);

    float cv[] = {1,2,3};
    Mat cM = newM(cv,3,1);
    
    Mat rowVec = getR(ma,1);
    prMat(rowVec);

    Mat colVec = getC(ma,1);
    prMat(colVec);

    printf("Product: %f\n\n",rxc(rM,cM));

    prMat(ma);
    int idx = 1;
    int jdx = 1;
    printf("\nElement at (%d, %d): %.4f\n",idx,jdx,getE(ma,idx,jdx));

    prMat(mul(ma,idenTT));

    printf("\nEnd of test\n______________________________\n");
    return;
}

void prMat(Mat inst)
{
    float *arr = inst->arr;
    int row = inst->h;
    int col = inst->w;

    printf("Instance: %dx%d\n",row,col);

    for(int i = 0;i<row;i++)
    {
        for(int j =0;j<col;j++)
        {
            printf("\t%.4f",arr[i*col+j]);
        }
        printf("\n");
    }
    return;
}

float getE(Mat m,int idx,int jdx)
{
    return m->arr[idx*m->w+jdx];
}

float rxc(Mat r,Mat c)
{
    if(r->w != c->h)
    {
        return NAN;
    }
    else
    {
        int sum = 0;
        for(int i = 0; i<r->w ; i++)
        {
            sum += r->arr[i]*c->arr[i];
        }
        return sum;
    }
}

Mat getR(Mat m,int R)
{
    float *result = malloc(m->w*sizeof(float));
    for(int i=0;i<m->w;i++)
    {
        result[i]=m->arr[R*m->w+i];
    }
    return newM(result,1,m->w);
}

Mat getC(Mat m,int C)
{
    float *result = malloc(m->h*sizeof(float));
    for(int i=0;i<m->h;i++)
    {
        result[i]=m->arr[C+m->w*i];
    }
    return newM(result,m->h,1);
}

Mat mul(Mat m1, Mat m2)
{
    float *result = malloc(sizeof(float)*m1->h*m2->w);
    for(int i=0;i<m1->h;i++)
    {
        for(int j=0;j<m2->w;j++)
        {
            result[i*m2->w+j]=rxc(getR(m1,i),getC(m2,j));
        }
    }
    
    return m1;
}