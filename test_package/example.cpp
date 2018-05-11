#include "lmdb.h"


int main(int argc, char const *argv[])
{
    MDB_env* env;

    mdb_env_create(&env);
    mdb_env_close(env);
    return 0;
}
