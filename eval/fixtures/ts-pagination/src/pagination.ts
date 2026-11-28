export function pageCount(totalItems: number, pageSize: number): number {
  return Math.floor(totalItems / pageSize);
}

export function pageSlice<T>(items: T[], page: number, pageSize: number): T[] {
  const start = (page - 1) * pageSize;
  return items.slice(start, start + pageSize);
}
