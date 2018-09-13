<template>
  <el-row>
    <el-col :span="3">
      <el-menu  :default-active="$route.path" router>
        <el-menu-item index="/org">部门</el-menu-item>
        <el-menu-item index="/org/role">角色</el-menu-item>
        <el-menu-item index="/org/member">人员</el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="21" class="container">
        <router-view></router-view>
    </el-col>
  </el-row>
</template>

<style>
  .container{
    padding:10px;
  }
</style>