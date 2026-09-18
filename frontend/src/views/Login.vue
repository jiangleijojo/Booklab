<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 28px">实验室预约系统</h1>
      <div style="margin-top: 5px; margin-bottom: 30px">基于Agent智能预约系统</div>

      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item label="Activity name">
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入账号"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item label="Password">
          <el-input
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            type="primary"
            size="large"
            style="width: 100%"
            @click="login"
            :loading="loadingValue"
          >
            登录
          </el-button>
          <div style="margin-top: 20px; text-align: right">
            还没有账号？请 <a style="color: var(--el-color-primary)" href="/register">注册</a>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import router from '@/router'
// import { ElMessageBox } from 'element-plus'

const form = reactive({
  username: '',
  password: ''
})

const loadingValue = ref(false)

const login = () => {
  loadingValue.value = true
  // 登录逻辑
  setTimeout(() => {
    // 模拟登录成功
    loadingValue.value = false
    ElMessage.success('登录成功')
    router.push('/manager/home')
  }, 2000)
}
</script>

<style>
.login-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.login-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  padding: 30px;
  background-color: #fff;
}
</style>
