import os
filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\data\api\AiApi.kt"
content = """package com.lanturn.app.data.api

import com.lanturn.app.data.models.CareerChatRequest
import com.lanturn.app.data.models.CareerChatResponse
import com.lanturn.app.data.models.ChatMessageDto
import com.lanturn.app.data.models.ChatThreadDto
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path
import kotlinx.serialization.Serializable

@Serializable
data class AiBaseResponse<T>(val data: T)

@Serializable
data class AiThreadsResponse(val items: List<ChatThreadDto>)

@Serializable
data class AiMessagesResponse(val items: List<ChatMessageDto>)

interface AiApi {
    @POST("ai/career-chat")
    suspend fun careerChat(@Body request: CareerChatRequest): AiBaseResponse<CareerChatResponse>

    @GET("ai/threads")
    suspend fun getThreads(): AiBaseResponse<AiThreadsResponse>

    @GET("ai/threads/{threadId}/messages")
    suspend fun getThreadMessages(@Path("threadId") threadId: String): AiBaseResponse<AiMessagesResponse>
}
"""
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

repo_filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\data\repositories\AiRepository.kt"
with open(repo_filepath, "r", encoding="utf-8") as f:
    repo_content = f.read()

repo_content = repo_content.replace("emit(safeApiCall { api.careerChat(request) })", "emit(safeApiCall { api.careerChat(request).data })")
repo_content = repo_content.replace("emit(safeApiCall { api.getThreads() })", "emit(safeApiCall { api.getThreads().data.items })")
repo_content = repo_content.replace("emit(safeApiCall { api.getThreadMessages(threadId) })", "emit(safeApiCall { api.getThreadMessages(threadId).data.items })")

with open(repo_filepath, "w", encoding="utf-8") as f:
    f.write(repo_content)